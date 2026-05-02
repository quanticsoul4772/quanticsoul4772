# quanticsoul4772

I build software at whatever layer the problem lives at. Most of my recent work is in LLM agent infrastructure. The repo list also spans game AI, security tooling, Unity, firmware forks, and cloud utilities.

## agent-harness-v2

An event-sourced Claude agent runtime I built that ships PRs to codebases across GitHub. Three processes share one SQLite file on a Hetzner VPS. It runs when I start it (not 24/7, API cost is a real constraint) and works through an operator-approved queue. Every interaction feeds a closed-loop learning system: successful patterns become teachings, failures become antibodies, hostile behavior tightens the fear-map.

<!-- RAWCELL_STATUS_START -->
Status: currently resting. [Request a run.](https://github.com/quanticsoul4772/agent-harness-v2/issues/new/choose)
<!-- RAWCELL_STATUS_END -->

### Merged contributions on repos I don't own

<!-- RECEIPTS_START -->
| Repo | Merged | Latest |
| --- | ---: | --- |
| `Evaliphy/evaliphy` | 4 | [#28](https://github.com/Evaliphy/evaliphy/pull/28) fix: reorganize reports into per-run timestamped directories |
| `lingdojo/kana-dojo` | 3 | [#13003](https://github.com/lingdojo/kana-dojo/pull/13003) content: add new trivia question |
| `AlphaSudo/zerodast` | 2 | [#86](https://github.com/AlphaSudo/zerodast/pull/86) docs: add CONTRIBUTING.md with full contributor workflow |
| `leticiv/tarot-reddit-compiler` | 1 | [#8](https://github.com/leticiv/tarot-reddit-compiler/pull/8) feat: add personal notes field to each interpretation |
| `adandeigor/AlgoLab` | 1 | [#9](https://github.com/adandeigor/AlgoLab/pull/9) feat: add --version flag to CLI |
| `chatvector-ai/chatvector-ai` | 1 | [#236](https://github.com/chatvector-ai/chatvector-ai/pull/236) fix(logging): route test logs to separate files when APP_EN... |

Last 12 merges (most recent first):

- `2026-04-21` [`Evaliphy/evaliphy#28`](https://github.com/Evaliphy/evaliphy/pull/28) fix: reorganize reports into per-run timestamped directories
- `2026-04-20` [`leticiv/tarot-reddit-compiler#8`](https://github.com/leticiv/tarot-reddit-compiler/pull/8) feat: add personal notes field to each interpretation
- `2026-04-20` [`adandeigor/AlgoLab#9`](https://github.com/adandeigor/AlgoLab/pull/9) feat: add --version flag to CLI
- `2026-04-20` [`Evaliphy/evaliphy#32`](https://github.com/Evaliphy/evaliphy/pull/32) feat(ci): add vitest code coverage analysis
- `2026-04-20` [`Evaliphy/evaliphy#40`](https://github.com/Evaliphy/evaliphy/pull/40) feat: add vitest code coverage with GitHub Actions reporting
- `2026-04-19` [`lingdojo/kana-dojo#13003`](https://github.com/lingdojo/kana-dojo/pull/13003) content: add new trivia question
- `2026-04-19` [`chatvector-ai/chatvector-ai#236`](https://github.com/chatvector-ai/chatvector-ai/pull/236) fix(logging): route test logs to separate files when APP_ENV=test
- `2026-04-19` [`Evaliphy/evaliphy#31`](https://github.com/Evaliphy/evaliphy/pull/31) fix(reporters): improve HTML report assertions section UX
- `2026-04-13` [`lingdojo/kana-dojo#13015`](https://github.com/lingdojo/kana-dojo/pull/13015) content: add new trivia question
- `2026-04-13` [`AlphaSudo/zerodast#86`](https://github.com/AlphaSudo/zerodast/pull/86) docs: add CONTRIBUTING.md with full contributor workflow
- `2026-04-13` [`AlphaSudo/zerodast#87`](https://github.com/AlphaSudo/zerodast/pull/87) docs: improve README badge and image alt text for accessibility (#83)
- `2026-04-13` [`lingdojo/kana-dojo#12944`](https://github.com/lingdojo/kana-dojo/pull/12944) feat(theme): add Lucky Bamboo theme
<!-- RECEIPTS_END -->

### What the agent has shipped, by category

<!-- CAPABILITIES_START -->
**CI / lint unblock**: 2 merged
  - [`Evaliphy/evaliphy#32`](https://github.com/Evaliphy/evaliphy/pull/32) feat(ci): add vitest code coverage analysis
  - [`Evaliphy/evaliphy#40`](https://github.com/Evaliphy/evaliphy/pull/40) feat: add vitest code coverage with GitHub Actions reporting

**Bug fix**: 3 merged
  - [`Evaliphy/evaliphy#28`](https://github.com/Evaliphy/evaliphy/pull/28) fix: reorganize reports into per-run timestamped directories
  - [`chatvector-ai/chatvector-ai#236`](https://github.com/chatvector-ai/chatvector-ai/pull/236) fix(logging): route test logs to separate files when APP_ENV=test
  - [`Evaliphy/evaliphy#31`](https://github.com/Evaliphy/evaliphy/pull/31) fix(reporters): improve HTML report assertions section UX
<!-- CAPABILITIES_END -->

### Cross-repo commit activity, last 12 months

<img alt="Contribution heatmap (light)" src="heatmap-light.svg#gh-light-mode-only" />
<img alt="Contribution heatmap (dark)" src="heatmap-dark.svg#gh-dark-mode-only" />

## A sampler of everything else

- [mcplint](https://github.com/quanticsoul4772/mcplint): Rust CLI for testing, fuzzing, and security-scanning MCP servers.
- [analytical-mcp](https://github.com/quanticsoul4772/analytical-mcp), [unified-thinking](https://github.com/quanticsoul4772/unified-thinking), and [mcp-reasoning](https://github.com/quanticsoul4772/mcp-reasoning): three different cuts at giving models structured reasoning primitives (TypeScript, Go, and a 15-tool reasoning server).
- [claw-code-parity](https://github.com/quanticsoul4772/claw-code-parity): Rust CLI agent-harness rewrite with a parity rubric, mock harness, and structural analysis tools.
- [bruno](https://github.com/quanticsoul4772/bruno) and [bruno-swarm](https://github.com/quanticsoul4772/bruno-swarm): neural behavior engineering framework (named after Giordano Bruno) and a multi-agent developer swarm built on top of it.
- [zeek-yara-integration](https://github.com/quanticsoul4772/zeek-yara-integration): network-security learning platform built on Zeek and YARA.
- [trellis-runpod-worker](https://github.com/quanticsoul4772/trellis-runpod-worker): serverless worker for TRELLIS text-to-3D mesh generation.
- [mesh-firmware](https://github.com/quanticsoul4772/mesh-firmware): personal fork of Meshtastic firmware.
- [battlecode2026](https://github.com/quanticsoul4772/battlecode2026) and [javabot](https://github.com/quanticsoul4772/javabot): MIT Battlecode competition bots.

Roughly a dozen more MCP servers across the ecosystem (Obsidian, Grafana, Bear, Roblox, macOS shell, GitHub, Exa, Langbase, and others). Open an issue if one looks useful and isn't obvious.

## Stack

Whatever the job wants. Most often TypeScript, Python, Rust, Go. Occasional C#, Java, C++. SQLite as default storage.
