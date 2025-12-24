# SOC Operations Center — Detection & SOAR Automation (Documentation)
**Creators/Team:** CyberSentinels

SOC Operations Center is an **academic project** that simulates a realistic internal SOC with automation:
**detection → orchestration → case management → enrichment → response → metrics**.

This repository is **documentation-first** and contains the artifacts used in the project:
- Wazuh detection rules (XML)
- Shuffle SOAR workflows (Markdown specs + sanitized export JSON)
- SOC operating model (lifecycle, severity, response policies, escalation, KPIs)
- Evidence (screenshots + demo video)
- Optional: AI audit automation notes (separate module)

## Quick navigation
- **Demo & evidence:** `demo/`
- **Architecture & diagrams:** `architecture/` and `architecture/diagrams/`
- **SOC process (lifecycle/policy/metrics):** `soc-process/`
- **MITRE mapping:** `mitre/mitre-mapping.md`
- **Shuffle workflows:** `shuffle/workflows/` (specs) and `shuffle/exports/` (sanitized exports)
- **Wazuh rules:** `wazuh/rules/` + `wazuh/wazuh-rules-catalog.md`
- **Automation scripts:** `automation/python/`

## What this proves (skills)
- **Detection engineering:** self-written + modified Wazuh rules, tested and wired to automation
- **SOAR engineering:** workflow-driven response with thresholds, IOC checks, dedupe/routing logic
- **IR operations:** Alert→Case handling, triage/investigation assignment, and analyst SOPs
- **Security tooling integration:** Wazuh, Shuffle, TheHive, Cortex, MISP, pfSense, AD, Velociraptor, Discord/Slack

## Evidence
- Screenshots: `demo/screenshots/`
- Demo video: `demo/demo-video.md`

## Diagram slots
- `architecture/diagrams/` (add PNG/SVG + source `.drawio`)

## Notes on secrets
Workflow exports are included for reproducibility, but **sensitive fields are redacted**. Use environment variables or a secure secret store for real deployments.
