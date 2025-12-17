# CyberSentinels — SOC Platform (Wazuh + Shuffle + TheHive + Cortex + MISP)

CyberSentinels is a student-driven initiative to build and operate a simulated Security Operations Center (SOC) that mirrors real-world enterprise security operations.

This repository is **upload-ready** and focuses on:
- Clear documentation (architecture, integrations, workflows, and rules)
- Exported Shuffle workflows (sanitized)
- Wazuh custom rules (as provided)
- Evidence (screenshots + demo video)

## What CyberSentinels delivers
- **Detection (Wazuh):** custom correlation rules for authentication failures, SSH brute-force, PowerShell suspicious activity, file integrity changes, and privilege escalation.
- **Orchestration (Shuffle):** alert intake from Wazuh via webhook and orchestration of case management, enrichment, notifications, and response.
- **Case Management (TheHive):** cases created/updated by Shuffle.
- **Enrichment (Cortex):** analyzers used include VirusTotal, Shodan, and DomainTools.
- **Threat Intel (MISP):** IOC correlation for Wazuh and TheHive.
- **Notifications:** Discord and Slack.
- **Response:** auto-block malicious IPs via a dedicated Shuffle workflow.

## Evidence
- Screenshots: `media/screenshots/`
- Demo video: `media/videos.md`

> Note: UI screenshots are a **mock-up for portfolio/demo purposes**. Metrics shown are simulated.

## Architecture
- Diagram slot: `docs/diagrams/architecture.png` (you will add your own)
- Documentation: `docs/architecture.md`

## Quick start for reviewers
1. Read `docs/architecture.md` and `docs/integrations.md`
2. Review Wazuh detections: `docs/wazuh-rules-catalog.md` + `rules/wazuh/source/`
3. Review SOAR workflows: `docs/soar-workflows.md` + `workflows/shuffle/`
4. Watch the demo video: `media/videos.md`

## Security note
Do not commit secrets/tokens. Store credentials in Shuffle secrets / environment variables. Redact internal IPs and usernames if required before publishing.
