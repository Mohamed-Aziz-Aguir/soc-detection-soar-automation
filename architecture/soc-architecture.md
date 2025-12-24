# SOC Architecture (High-Level)

## Components
- **Wazuh** (SIEM / detection + agents)
- **Shuffle** (SOAR orchestration)
- **TheHive** (case management)
- **Cortex** (enrichment analyzers)
- **MISP** (threat intel)
- **pfSense** (network enforcement)
- **Active Directory** (identity controls)
- **Velociraptor** (endpoint containment/forensics)
- **Discord/Slack** (notifications)

## Data Flow (Narrative)
1. Wazuh generates an alert from logs/rules.
2. Wazuh forwards alert to Shuffle via webhook.
3. Shuffle normalizes payload and routes to workflow.
4. Workflow creates TheHive alert → case.
5. Cortex runs enrichments based on observables (IP/domain/url/hash).
6. Response actions execute (pfSense/AD/Velociraptor) based on severity & IOC confidence.
7. Analyst notified; case updated and tracked to closure.

## Diagrams
- `architecture/diagrams/`
