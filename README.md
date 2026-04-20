# quanticsoul4772

I build software at whatever layer the problem lives at. Most of my recent work is in LLM agent infrastructure. The repo list also spans game AI, security tooling, Unity, firmware forks, and cloud utilities.

## rawcell-agent

An autonomous Claude agent I built that ships PRs to codebases across GitHub. It runs on a Hetzner VPS when I start it (not 24/7, API cost is a real constraint) and works through an operator-approved queue. Every interaction feeds a closed-loop learning system: successful patterns become teachings, failures become antibodies, hostile behavior tightens the fear-map.

<!-- RAWCELL_STATUS_START -->
Status: currently resting. [Request a run.](https://github.com/quanticsoul4772/rawcell-agent/issues/new/choose)
<!-- RAWCELL_STATUS_END -->

### Merged contributions on repos I don't own

<!-- RECEIPTS_START -->
| Repo | Merged | Latest |
| --- | ---: | --- |
| `danesjenovdan/parlameter` | 12 | [#1939](https://github.com/danesjenovdan/parlameter/pull/1939) Pulling refs/heads/dev into zagreb |
| `233XvX233/Silksong-Steam-multiplayer-mod-data` | 6 | [#16886](https://github.com/233XvX233/Silksong-Steam-multiplayer-mod-data/pull/16886) Auto-append feedback to comments.txt |
| `Josefjosefjosef/filtr` | 5 | [#2961](https://github.com/Josefjosefjosef/filtr/pull/2961) chore(data): update articles data |
| `OwenNolis/Jira-Autofix` | 5 | [#24](https://github.com/OwenNolis/Jira-Autofix/pull/24) [JIRAFIX-13] [JIRAFIX-13] Change the footer text to Powered... |
| `flexera-public/policy_templates` | 4 | [#4360](https://github.com/flexera-public/policy_templates/pull/4360) Update Active Policy List |
| `elastic/ems-landing-page` | 4 | [#3492](https://github.com/elastic/ems-landing-page/pull/3492) [v9.4] chore: remove redundant lodash resolution (#3419) |
| `mandarini/repro-nx-release` | 3 | [#38](https://github.com/mandarini/repro-nx-release/pull/38) [patchback] feat: four |
| `marckraw/convergence` | 3 | [#60](https://github.com/marckraw/convergence/pull/60) Version Packages |
| `spacesprotocol/certrelay` | 2 | [#64](https://github.com/spacesprotocol/certrelay/pull/64) chore: release v0.1.2 |
| `peetzweg/polkadot-cli` | 2 | [#178](https://github.com/peetzweg/polkadot-cli/pull/178) Version Packages |
| `GioPat/gp-grid` | 2 | [#52](https://github.com/GioPat/gp-grid/pull/52) chore(master): release gp-grid 0.11.2 |
| `Castro-Media/TopStoryReview.com` | 2 | [#6725](https://github.com/Castro-Media/TopStoryReview.com/pull/6725) Automated data update |

Last 12 merges (most recent first):

- `2026-04-20` [`lukso-network/tools-web-components#848`](https://github.com/lukso-network/tools-web-components/pull/848) chore(main): release 1.191.0
- `2026-04-20` [`spacesprotocol/certrelay#64`](https://github.com/spacesprotocol/certrelay/pull/64) chore: release v0.1.2
- `2026-04-20` [`JagPat/Vitan-BrandBuilding#320`](https://github.com/JagPat/Vitan-BrandBuilding/pull/320) [workdrive-sync] Update WorkDrive sync state
- `2026-04-20` [`mandarini/repro-nx-release#38`](https://github.com/mandarini/repro-nx-release/pull/38) [patchback] feat: four
- `2026-04-20` [`UtePabst/UtePabst#542`](https://github.com/UtePabst/UtePabst/pull/542) [Automated] Update README with new chess puzzle
- `2026-04-20` [`yorbapro/smart-neighbor-grow#20`](https://github.com/yorbapro/smart-neighbor-grow/pull/20) New AI News Article: Nuance Launches Dragon Voice Assistant 5.0 with Breakthrou...
- `2026-04-20` [`MatthiasReinholz/wp-plugin-base#100`](https://github.com/MatthiasReinholz/wp-plugin-base/pull/100) Foundation release v1.7.6
- `2026-04-20` [`stefanko-ch/Nexus-Stack-for-Education#21`](https://github.com/stefanko-ch/Nexus-Stack-for-Education/pull/21) chore(main): release 1.2.0
- `2026-04-20` [`ministryofjustice/modernisation-platform#12967`](https://github.com/ministryofjustice/modernisation-platform/pull/12967) New files for terraform/environments
- `2026-04-20` [`vamsi4162/vamsi4162.github.io#1`](https://github.com/vamsi4162/vamsi4162.github.io/pull/1) Update portfolio website from resume
- `2026-04-20` [`Josefjosefjosef/filtr#2961`](https://github.com/Josefjosefjosef/filtr/pull/2961) chore(data): update articles data
- `2026-04-20` [`aliou/pi-neuralwatt#1`](https://github.com/aliou/pi-neuralwatt/pull/1) Updating @aliou/pi-neuralwatt to version 0.1.0
<!-- RECEIPTS_END -->

### What the agent has shipped, by category

<!-- CAPABILITIES_START -->
**Dep bump / lockfile**: 6 merged
  - [`fink-lang/homebrew-tap#19`](https://github.com/fink-lang/homebrew-tap/pull/19) chore: bump fink to v0.57.0
  - [`yanosea/yanoNixFiles#1356`](https://github.com/yanosea/yanoNixFiles/pull/1356) ⚡deps(nix): update dependencies in `flake.lock` (2026-04-21)
  - [`fern-api/fern#15171`](https://github.com/fern-api/fern/pull/15171) chore(php): regenerate php-model seeds to pick up phpunit 12.5.22 bump
  - [`habitat-sh/chef-habitat-docs#97`](https://github.com/habitat-sh/chef-habitat-docs/pull/97) [release-2.0] Bump habitat docs content to latest stable release (d98...

**CI / lint unblock**: 7 merged
  - [`NASA-IMPACT/veda-config#979`](https://github.com/NASA-IMPACT/veda-config/pull/979) ci: Update submodule to version v6.20.7
  - [`TheLarkInn/aipm#601`](https://github.com/TheLarkInn/aipm/pull/601) [coverage-improver] Cover detect() read_to_string error propagation i...
  - [`akporto/pix-payment-engine#2`](https://github.com/akporto/pix-payment-engine/pull/2) ci: [Auto-PR] Integration of branch feature/pix-payment-engine
  - [`Sebenza-Hub-V001/Sebenza_Hub_Claude_V2#376`](https://github.com/Sebenza-Hub-V001/Sebenza_Hub_Claude_V2/pull/376) Auto-deploy: Enhance applicant detail view documentation with Playwri...

**Bug fix**: 2 merged
  - [`BV-BRC/BV-BRC-Web#1278`](https://github.com/BV-BRC/BV-BRC-Web/pull/1278) Hotfix v3.57.30
  - [`mandarini/repro-nx-release#29`](https://github.com/mandarini/repro-nx-release/pull/29) [patchback] fix: four
<!-- CAPABILITIES_END -->

### Cross-repo commit activity, last 12 months

<img alt="Contribution heatmap (light)" src="heatmap-light.svg#gh-light-mode-only" />
<img alt="Contribution heatmap (dark)" src="heatmap-dark.svg#gh-dark-mode-only" />

## Flagship

[agent-harness-v2](https://github.com/quanticsoul4772/agent-harness-v2): event-sourced runtime for a long-running Claude agent. Three processes share one SQLite file. The event log is the source of truth, projections are rebuildable, and safety gates are enforced in code rather than prompted.

## A sampler of everything else

- [mcplint](https://github.com/quanticsoul4772/mcplint): Rust CLI for testing, fuzzing, and security-scanning MCP servers.
- [analytical-mcp](https://github.com/quanticsoul4772/analytical-mcp) and [unified-thinking](https://github.com/quanticsoul4772/unified-thinking): two different cuts at giving models structured reasoning primitives (TypeScript, Go).
- [bruno](https://github.com/quanticsoul4772/bruno): neural behavior engineering framework, named after Giordano Bruno.
- [zeek-yara-integration](https://github.com/quanticsoul4772/zeek-yara-integration): network-security learning platform built on Zeek and YARA.
- [trellis-runpod-worker](https://github.com/quanticsoul4772/trellis-runpod-worker): serverless worker for TRELLIS text-to-3D mesh generation.
- [mesh-firmware](https://github.com/quanticsoul4772/mesh-firmware): personal fork of Meshtastic firmware.
- [battlecode2026](https://github.com/quanticsoul4772/battlecode2026) and [javabot](https://github.com/quanticsoul4772/javabot): MIT Battlecode competition bots.
- [ec2sensor](https://github.com/quanticsoul4772/ec2sensor): Go CLI for live EC2 sensor metrics.

Roughly 15 more MCP servers across the ecosystem (Obsidian, Grafana, Bear, Roblox, macOS shell, GitHub, Exa, Langbase, and others). Open an issue if one looks useful and isn't obvious.

## Stack

Whatever the job wants. Most often TypeScript, Python, Rust, Go. Occasional C#, Java, C++. SQLite as default storage.
