# SOC Detection & SOAR Automation Portfolio (Wazuh + Shuffle + TheHive + Cortex + MISP)

This repository documents an end-to-end SOC pipeline that transforms SIEM detections into incident handling via SOAR orchestration, case management, and automated enrichment.

**Scope:** This repo provides documentation, configuration artifacts (sanitized), workflow exports, and evidence (screenshots + video). It does **not** provide a one-click redeployment of the entire environment.

## What this project demonstrates
- **Detection engineering (Wazuh):** custom rules/correlation for events such as SSH brute-force, privilege escalation, and login failures
- **SOAR automation (Shuffle):** webhook-driven orchestration for alert routing, case handling, notifications, and response actions
- **Case management (TheHive):** structured incident tracking with tasks/observables (created/updated via Shuffle)
- **Automated enrichment (Cortex):** analyzers for IP/domain/URL/file enrichment (e.g., VirusTotal, Shodan, DomainTools)
- **Threat intelligence (MISP):** IOC correlation to enrich Wazuh alerts and TheHive cases
- **SOC operations thinking:** health visibility, incident lifecycle, and audit-ready documentation

## Evidence (Option A)
- Screenshots: `media/screenshots/`
- Demo video: `media/videos.md`

> Note: Any dashboard/UI shown in screenshots is a **mock-up used for demonstration**. Metrics and tool statuses shown are simulated for portfolio purposes.

## Architecture
See `docs/architecture.md` for the full data flow and trust boundaries.

## Operational defaults used in this project
- Severity mapping (Wazuh `rule.level` → severity):
  - **Low:** 0–7
  - **Medium:** 8–12
  - **High:** 13–16
- Notifications: **Discord** and **Slack**
- Response: **auto-block malicious IPs** via a dedicated Shuffle workflow
- Deduplication: implemented in Shuffle using a **counter/guard script** to avoid duplicate executions for the same recurring attack pattern

## Repository map
- `docs/` — architecture, integrations, detection engineering, SOAR workflow specs, IR process, lessons learned
- `rules/wazuh/` — Wazuh rule artifacts (sanitized)
- `workflows/shuffle/` — Shuffle workflow exports (JSON; sanitized)
- `media/` — screenshots and demo video link

## Security note
Do not commit secrets/tokens. Store credentials in Shuffle secrets / environment variables and redact exports before publishing.
