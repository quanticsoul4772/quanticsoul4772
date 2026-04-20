"""Regenerate the dynamic blocks of README.md from live GitHub data.

Blocks updated:
  RECEIPTS     — table of merged PRs on repos not owned by the profile user.
  CAPABILITIES — four-category breakdown with PR-link receipts per category.
  HEATMAP      — 52x7 SVG of commit counts per day over the last year, theme-aware.

The script is idempotent: if nothing has changed since the last run, the
README file content will be byte-identical.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

USER = "quanticsoul4772"
README = Path(__file__).resolve().parent.parent / "README.md"
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


# --- GitHub calls via gh CLI (inherits auth from the workflow) ---

def gh(*args: str) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(f"gh {' '.join(args)} failed: {result.stderr}\n")
        sys.exit(1)
    return result.stdout


def fetch_external_merged_prs() -> list[Pr]:
    """Every PR @me has merged on a repo NOT owned by @me."""
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
    """Daily commit counts for the last year via GraphQL contributionsCollection."""
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


# --- Categorization ---

CATEGORIES: list[tuple[str, list[str]]] = [
    ("Conflict resolution", ["conflict", "rebase", "merge conflict", "resolves #", "resolve #"]),
    ("Dep bump / lockfile",  ["bump", "dep(", "deps:", "deps(", "chore(deps)", "lockfile", "lock file"]),
    ("CI / lint unblock",    ["lint", "eslint", "ci:", "ci(", "coverage", "pnpm-lock", ".github/workflows"]),
    ("Bug fix",              ["fix:", "fix(", "bug", "crash", "regression", "hotfix"]),
]


def categorize(pr: Pr) -> str | None:
    title_lower = pr.title.lower()
    for name, keywords in CATEGORIES:
        if any(k in title_lower for k in keywords):
            return name
    return None


# --- Block rendering ---

def render_receipts(prs: list[Pr]) -> str:
    if not prs:
        return "_No merged external-repo PRs yet._"

    recent = prs[:RECEIPTS_LIMIT]
    by_repo: dict[str, list[Pr]] = defaultdict(list)
    for p in prs:
        by_repo[p.repo].append(p)

    repo_summary: list[tuple[str, int, Pr]] = [
        (repo, len(items), items[0]) for repo, items in by_repo.items()
    ]
    repo_summary.sort(key=lambda row: (-row[1], row[2].merged_at.isoformat()), reverse=False)
    repo_summary.sort(key=lambda row: -row[1])

    lines = ["| Repo | Merged | Latest |", "| --- | ---: | --- |"]
    for repo, count, latest in repo_summary[:RECEIPTS_LIMIT]:
        bar = "█" * min(count, 6)
        latest_link = f"[#{latest.number}]({latest.url})"
        lines.append(f"| `{repo}` | {bar} {count} | {latest_link} {_truncate(latest.title, 60)} |")

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
        header = f"**{name}** — {len(items)} merged"
        sample = items[:CATEGORY_LIMIT]
        bullet_lines = [
            f"  - [`{p.repo}#{p.number}`]({p.url}) {_truncate(p.title, 70)}" for p in sample
        ]
        blocks.append(header + "\n" + "\n".join(bullet_lines))
    return "\n\n".join(blocks)


def render_heatmap(days: list[tuple[date, int]]) -> str:
    """Render a 52w x 7d contribution heatmap as inline SVG (theme-aware)."""
    if not days:
        return "_No contribution data available._"

    days.sort(key=lambda row: row[0])
    days = days[-HEATMAP_WEEKS * 7:]

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

    light_palette = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
    dark_palette  = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

    weeks: list[list[tuple[date, int]]] = []
    current: list[tuple[date, int]] = []
    anchor_dow = days[0][0].weekday()
    for _ in range(anchor_dow):
        current.append((None, 0))  # type: ignore[arg-type]
    for d, c in days:
        current.append((d, c))
        if len(current) == 7:
            weeks.append(current)
            current = []
    if current:
        while len(current) < 7:
            current.append((None, 0))  # type: ignore[arg-type]
        weeks.append(current)
    weeks = weeks[-HEATMAP_WEEKS:]

    rects_light: list[str] = []
    rects_dark: list[str] = []
    for wi, week in enumerate(weeks):
        x = left_pad + wi * (cell + gap)
        for di, (d, c) in enumerate(week):
            y = top_pad + di * (cell + gap)
            if d is None:
                continue
            lvl = level(c)
            title = f"{d.isoformat()}: {c} contribution{'s' if c != 1 else ''}"
            rects_light.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" ry="2" '
                f'fill="{light_palette[lvl]}"><title>{title}</title></rect>'
            )
            rects_dark.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" ry="2" '
                f'fill="{dark_palette[lvl]}"><title>{title}</title></rect>'
            )

    day_labels: list[str] = []
    for i, name in enumerate(["Mon", "Wed", "Fri"]):
        row = i * 2 + 1
        y = top_pad + row * (cell + gap) + cell - 2
        day_labels.append(
            f'<text x="0" y="{y}" font-family="Segoe UI, system-ui, sans-serif" '
            f'font-size="10" fill="currentColor">{name}</text>'
        )

    total = sum(c for _, c in days)
    summary = (
        f'<text x="{left_pad}" y="12" font-family="Segoe UI, system-ui, sans-serif" '
        f'font-size="11" fill="currentColor">{total:,} contributions, last {len(days)} days</text>'
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Contribution heatmap">
  <style>
    :root {{ color: #1f2328; }}
    @media (prefers-color-scheme: dark) {{ :root {{ color: #e6edf3; }} .light {{ display: none; }} .dark {{ display: inline; }} }}
    @media (prefers-color-scheme: light) {{ .dark {{ display: none; }} .light {{ display: inline; }} }}
    .dark {{ display: none; }}
  </style>
  {summary}
  {"".join(day_labels)}
  <g class="light">{"".join(rects_light)}</g>
  <g class="dark">{"".join(rects_dark)}</g>
</svg>"""

    return svg


# --- Marker replacement ---

def _truncate(text: str, n: int) -> str:
    text = text.strip().replace("|", "\\|")
    return text if len(text) <= n else text[: n - 1] + "…"


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
    heatmap = render_heatmap(days)

    content = README.read_text(encoding="utf-8")
    content = replace_block(content, "RECEIPTS", receipts)
    content = replace_block(content, "CAPABILITIES", capabilities)
    content = replace_block(content, "HEATMAP", heatmap)
    README.write_text(content, encoding="utf-8")

    print(f"Receipts:     {len(prs)} external-repo PRs")
    print(f"Contribution days: {len(days)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
