# SOC Operations Center — Documentation Repository
**Creators/Team:** CyberSentinels

SOC Operations Center is an **academic project** that simulates a realistic internal SOC, demonstrating end-to-end SOC engineering:
detection → orchestration → case management → enrichment → response → metrics.

This repository is **documentation-first** and includes the artifacts used in the project:
- Wazuh rule XML files
- Shuffle SOAR workflow exports
- Process documentation (architecture, response policies, playbooks, metrics)
- Evidence (screenshots + demo video link)

## What this proves (skills)
- **Detection engineering:** self-written + modified Wazuh rules, tested and wired to automation
- **SOAR engineering:** workflow-driven response with thresholds, IOC checks, partial dedupe, and routing logic
- **IR operations:** Alert→Case handling, triage/investigation assignment, and manual rollback simulation
- **Security tooling integration:** Wazuh, Shuffle, TheHive, Cortex, MISP, pfSense, AD, Velociraptor, Discord/Slack

## Evidence
- Screenshots: `assets/screenshots/`
- Demo video: `docs/demo-video.md`

## Diagram slots
- `docs/diagrams/architecture.png`
- `docs/diagrams/network-zones.png`
- `docs/diagrams/workflow-sequence.png`

## Repository layout
- `docs/` — documentation (architecture, integrations, workflows, playbooks, metrics, roadmap)
- `wazuh/rules/` — Wazuh rule XML files
- `shuffle/workflows/` — Shuffle workflow export JSONs
- `automation/python/` — custom Python utilities (parsing, dedupe, routing, pfSense API calls)

## Key design choices
- TheHive flow: **Alert → Case**
- Enrichment: **Case then enrich** (Cortex analyzers)
- IOC types used: domain / URL / hash / srcip
- Metrics: **real**, pulled from tool APIs (as used in the project)

## Notes on credentials
Publishing real credentials is unsafe. This repo keeps automation code **production-style** by using environment variables for secrets.
