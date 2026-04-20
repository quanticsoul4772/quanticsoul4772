"""Regenerate the dynamic blocks of README.md from live GitHub data.

Updates:
  RECEIPTS     : table of merged PRs on repos not owned by the profile user.
  CAPABILITIES : four-category breakdown with PR-link samples per category.
  heatmap-light.svg / heatmap-dark.svg : 52x7 commit-count grid per day
    over the last year, written as separate files so GitHub renders them
    via <img src="...svg#gh-{light,dark}-mode-only">. Inline SVG inside
    markdown is sanitized by GitHub and will not render.

The script is idempotent: if nothing has changed, README.md and the two
SVG files come out byte-identical.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

USER = "quanticsoul4772"
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
HEATMAP_LIGHT = ROOT / "heatmap-light.svg"
HEATMAP_DARK = ROOT / "heatmap-dark.svg"
RECEIPTS_LIMIT = 12
CATEGORY_LIMIT = 4
HEATMAP_WEEKS = 52


@dataclass(frozen=True)
class Pr:
    repo: str
    number: int
    title: str
    url: str
    merged_at: datetime


def gh(*args: str) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(f"gh {' '.join(args)} failed: {result.stderr}\n")
        sys.exit(1)
    return result.stdout


def fetch_external_merged_prs() -> list[Pr]:
    raw = gh(
        "search", "prs",
        "--author", "@me",
        "--merged",
        "--limit", "200",
        "--json", "repository,number,title,url,updatedAt",
    )
    items = json.loads(raw)
    prs: list[Pr] = []
    for it in items:
        repo = it["repository"]["nameWithOwner"]
        if repo.split("/")[0] == USER:
            continue
        prs.append(Pr(
            repo=repo,
            number=int(it["number"]),
            title=it["title"],
            url=it["url"],
            merged_at=datetime.fromisoformat(it["updatedAt"].replace("Z", "+00:00")),
        ))
    prs.sort(key=lambda p: p.merged_at, reverse=True)
    return prs


def fetch_contribution_calendar() -> list[tuple[date, int]]:
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            weeks { contributionDays { date contributionCount } }
          }
        }
      }
    }
    """
    raw = gh(
        "api", "graphql",
        "-f", f"query={query}",
        "-F", f"login={USER}",
    )
    data = json.loads(raw)
    out: list[tuple[date, int]] = []
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    for w in weeks:
        for d in w["contributionDays"]:
            out.append((date.fromisoformat(d["date"]), int(d["contributionCount"])))
    return out


CATEGORIES: list[tuple[str, list[str]]] = [
    ("Conflict resolution", ["conflict", "rebase", "merge conflict", "resolves #", "resolve #"]),
    ("Dep bump / lockfile", ["bump", "dep(", "deps:", "deps(", "chore(deps)", "lockfile", "lock file"]),
    ("CI / lint unblock",   ["lint", "eslint", "ci:", "ci(", "coverage", "pnpm-lock", ".github/workflows"]),
    ("Bug fix",             ["fix:", "fix(", "bug", "crash", "regression", "hotfix"]),
]


def categorize(pr: Pr) -> str | None:
    title_lower = pr.title.lower()
    for name, keywords in CATEGORIES:
        if any(k in title_lower for k in keywords):
            return name
    return None


def _truncate(text: str, n: int) -> str:
    text = text.strip().replace("|", "\\|")
    return text if len(text) <= n else text[: n - 1] + "..."


def render_receipts(prs: list[Pr]) -> str:
    if not prs:
        return "_No merged external-repo PRs yet._"

    recent = prs[:RECEIPTS_LIMIT]
    by_repo: dict[str, list[Pr]] = defaultdict(list)
    for p in prs:
        by_repo[p.repo].append(p)

    repo_summary = [(repo, len(items), items[0]) for repo, items in by_repo.items()]
    repo_summary.sort(key=lambda row: -row[1])

    lines = ["| Repo | Merged | Latest |", "| --- | ---: | --- |"]
    for repo, count, latest in repo_summary[:RECEIPTS_LIMIT]:
        latest_link = f"[#{latest.number}]({latest.url})"
        lines.append(f"| `{repo}` | {count} | {latest_link} {_truncate(latest.title, 60)} |")

    lines.append("")
    lines.append(f"Last {len(recent)} merges (most recent first):")
    lines.append("")
    for p in recent:
        ts = p.merged_at.strftime("%Y-%m-%d")
        lines.append(f"- `{ts}` [`{p.repo}#{p.number}`]({p.url}) {_truncate(p.title, 80)}")
    return "\n".join(lines)


def render_capabilities(prs: list[Pr]) -> str:
    buckets: dict[str, list[Pr]] = defaultdict(list)
    for p in prs:
        cat = categorize(p)
        if cat:
            buckets[cat].append(p)

    if not buckets:
        return "_Not enough categorized PRs yet._"

    blocks: list[str] = []
    for name, _ in CATEGORIES:
        items = buckets.get(name, [])
        if not items:
            continue
        header = f"**{name}**: {len(items)} merged"
        sample = items[:CATEGORY_LIMIT]
        bullet_lines = [
            f"  - [`{p.repo}#{p.number}`]({p.url}) {_truncate(p.title, 70)}" for p in sample
        ]
        blocks.append(header + "\n" + "\n".join(bullet_lines))
    return "\n\n".join(blocks)


def _build_heatmap_svg(days: list[tuple[date, int]], palette: list[str], text_color: str) -> str:
    cell = 12
    gap = 3
    left_pad = 28
    top_pad = 18
    width = left_pad + HEATMAP_WEEKS * (cell + gap)
    height = top_pad + 7 * (cell + gap)

    max_count = max((c for _, c in days), default=0)

    def level(n: int) -> int:
        if n == 0:
            return 0
        if max_count <= 1:
            return 4
        ratio = n / max_count
        if ratio < 0.25:
            return 1
        if ratio < 0.5:
            return 2
        if ratio < 0.75:
            return 3
        return 4

    weeks: list[list[tuple[date | None, int]]] = []
    current: list[tuple[date | None, int]] = []
    anchor_dow = days[0][0].weekday()
    for _ in range(anchor_dow):
        current.append((None, 0))
    for d, c in days:
        current.append((d, c))
        if len(current) == 7:
            weeks.append(current)
            current = []
    if current:
        while len(current) < 7:
            current.append((None, 0))
        weeks.append(current)
    weeks = weeks[-HEATMAP_WEEKS:]

    rects: list[str] = []
    for wi, week in enumerate(weeks):
        x = left_pad + wi * (cell + gap)
        for di, (d, c) in enumerate(week):
            y = top_pad + di * (cell + gap)
            if d is None:
                continue
            lvl = level(c)
            plural = "s" if c != 1 else ""
            title = f"{d.isoformat()}: {c} contribution{plural}"
            rects.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" ry="2" '
                f'fill="{palette[lvl]}"><title>{title}</title></rect>'
            )

    day_labels: list[str] = []
    for i, name in enumerate(["Mon", "Wed", "Fri"]):
        row = i * 2 + 1
        y = top_pad + row * (cell + gap) + cell - 2
        day_labels.append(
            f'<text x="0" y="{y}" font-family="Segoe UI, system-ui, sans-serif" '
            f'font-size="10" fill="{text_color}">{name}</text>'
        )

    total = sum(c for _, c in days)
    summary = (
        f'<text x="{left_pad}" y="12" font-family="Segoe UI, system-ui, sans-serif" '
        f'font-size="11" fill="{text_color}">{total:,} contributions, last {len(days)} days</text>'
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
        f'role="img" aria-label="Contribution heatmap">'
        f'{summary}{"".join(day_labels)}{"".join(rects)}</svg>'
    )


def write_heatmaps(days: list[tuple[date, int]]) -> None:
    days = sorted(days, key=lambda row: row[0])[-HEATMAP_WEEKS * 7:]
    if not days:
        HEATMAP_LIGHT.write_text("", encoding="utf-8")
        HEATMAP_DARK.write_text("", encoding="utf-8")
        return

    light_palette = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
    dark_palette  = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

    HEATMAP_LIGHT.write_text(
        _build_heatmap_svg(days, light_palette, "#1f2328"),
        encoding="utf-8",
    )
    HEATMAP_DARK.write_text(
        _build_heatmap_svg(days, dark_palette, "#e6edf3"),
        encoding="utf-8",
    )


def replace_block(content: str, tag: str, new_body: str) -> str:
    pattern = re.compile(
        rf"(<!-- {tag}_START -->)(.*?)(<!-- {tag}_END -->)",
        re.DOTALL,
    )
    replacement = rf"\g<1>\n{new_body}\n\g<3>"
    return pattern.sub(replacement, content)


def main() -> int:
    prs = fetch_external_merged_prs()
    days = fetch_contribution_calendar()

    receipts = render_receipts(prs)
    capabilities = render_capabilities(prs)

    content = README.read_text(encoding="utf-8")
    content = replace_block(content, "RECEIPTS", receipts)
    content = replace_block(content, "CAPABILITIES", capabilities)
    README.write_text(content, encoding="utf-8")

    write_heatmaps(days)

    print(f"Receipts: {len(prs)} external-repo PRs")
    print(f"Contribution days: {len(days)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
