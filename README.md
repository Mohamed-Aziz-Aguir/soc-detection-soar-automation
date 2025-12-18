# SOC Operations Center — Documentation Repository
**Creators/Team:** CyberSentinels

This repository documents the **SOC Operations Center** academic project: a realistic internal SOC design with automation, enrichment, and response paths.

It includes:
- Wazuh custom rules used in the project
- Shuffle SOAR workflow exports
- Documentation (architecture, integrations, playbooks, metrics)
- Evidence (screenshots + demo video link)

## High-level capabilities
- **Detection:** Wazuh correlation rules (Linux + Windows + file integrity)
- **SOAR:** Shuffle orchestration (severity mapping, routing, partial dedupe, conditional response)
- **Case management:** TheHive (Alert → Case)
- **Enrichment:** Cortex analyzers (VirusTotal, Shodan, DomainTools)
- **Threat intel:** MISP IOC correlation (influences severity/response)
- **Response paths (conditional):** pfSense blocking, Active Directory actions, Velociraptor quarantine
- **Notifications:** Discord and Slack

## Evidence
- Screenshots: `assets/screenshots/`
- Demo video: `docs/demo-video.md`

## Diagram slots
Add your own diagrams here:
- `docs/diagrams/architecture.png`
- `docs/diagrams/network-zones.png`
- `docs/diagrams/workflow-sequence.png`

## Repository contents
- `docs/` — documentation (architecture, integrations, workflows, playbooks, metrics, roadmap)
- `wazuh/rules/` — Wazuh rule XML files
- `shuffle/workflows/` — Shuffle workflow export JSONs
- `automation/python/` — documentation slot for the custom Python logic used in handling conditions/repeated tasks

## Defaults used in this project
- Severity mapping (Wazuh `rule.level`):
  - Low: 0–7
  - Medium: 8–12
  - High: 13–16
- Dedupe key (where implemented): `rule.id + srcip + agent.name`
- Enrichment executed **after** case creation (Case then enrich)

## Notes
This is a **documentation-first** repository created for portfolio and review purposes.
