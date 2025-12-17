# Architecture (CyberSentinels SOC)

## Core flow (logical)
- **Wazuh → Shuffle:** Wazuh sends alerts to Shuffle via webhook.
- **Shuffle → TheHive:** Shuffle creates/updates TheHive cases and attaches observables.
- **TheHive → Cortex:** TheHive triggers Cortex analyzers; results are added to the case.
- **MISP → Wazuh & TheHive:** IOC enrichment and correlation.
- **Shuffle → Discord/Slack:** notifications and escalation.
- **Shuffle → Firewall:** automated response via IP block workflow (when applicable).

## Diagram
Add your diagram here:
- `docs/diagrams/architecture.png`

(Keep a short caption under it once added.)

## Severity mapping used
Based on Wazuh `rule.level`:
- Low: **0–7**
- Medium: **8–12**
- High: **13–16**

## Deduplication approach
To avoid flooding the SOC channels, Shuffle workflows include a counter/guard step to avoid sending repeated notifications for the same recurring attack pattern.

## Environment context (lab)
The environment was deployed in a segmented lab (multi-zone networking with firewalls), integrating SIEM, SOAR, case management, enrichment, endpoint visibility, and NIDS tooling.
