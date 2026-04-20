# quanticsoul4772

I build software at whatever layer the problem lives at. Most of my recent work is in LLM agent infrastructure, but the repo list also spans game AI, security tooling, Unity, firmware forks, and cloud utilities. I like finishing things, so almost everything here works.

## Flagship

**[agent-harness-v2](https://github.com/quanticsoul4772/agent-harness-v2)** — event-sourced runtime for a long-running Claude agent. Three processes share one SQLite file; the event log is the source of truth, projections are rebuildable, and safety gates are enforced in code rather than prompted. Runs autonomously on a VPS.

## A sampler of everything else

- **[mcplint](https://github.com/quanticsoul4772/mcplint)** — Rust CLI for testing, fuzzing, and security-scanning MCP servers.
- **[analytical-mcp](https://github.com/quanticsoul4772/analytical-mcp)** / **[unified-thinking](https://github.com/quanticsoul4772/unified-thinking)** — two different cuts at giving models structured reasoning primitives (TypeScript, Go).
- **[bruno](https://github.com/quanticsoul4772/bruno)** — neural behavior engineering framework; named after Giordano Bruno.
- **[zeek-yara-integration](https://github.com/quanticsoul4772/zeek-yara-integration)** — educational platform for network security using Zeek + YARA.
- **[trellis-runpod-worker](https://github.com/quanticsoul4772/trellis-runpod-worker)** — serverless worker for TRELLIS text-to-3D mesh generation.
- **[mesh-firmware](https://github.com/quanticsoul4772/mesh-firmware)** — personal fork of Meshtastic firmware.
- **[battlecode2026](https://github.com/quanticsoul4772/battlecode2026)** / **[javabot](https://github.com/quanticsoul4772/javabot)** — MIT Battlecode competition bots.
- **[ec2sensor](https://github.com/quanticsoul4772/ec2sensor)** — Go CLI for live EC2 sensor metrics.

Roughly 15 more MCP servers across the ecosystem (Obsidian, Grafana, Bear, Roblox, macOS shell, GitHub, Exa, Langbase, ...). Open an issue if one looks useful and isn't obvious.

## Stack

Whatever the job wants. Most often TypeScript, Python, Rust, Go; occasional C#, Java, C++. SQLite as default storage.
