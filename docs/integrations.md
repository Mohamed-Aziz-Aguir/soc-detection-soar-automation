# Integrations

This section describes the logical integrations between tools. Exact endpoint URLs and tokens are intentionally not included in the repo and should be stored as secrets.

## Wazuh → Shuffle (Webhook trigger)
**Goal:** Real-time orchestration for routing, case handling, enrichment, notifications, and response.
- Wazuh sends selected alerts to a Shuffle webhook.
- Shuffle normalizes the alert payload, applies decision logic, and triggers actions.

**Webhook security (recommended)**
- Shared secret header OR HMAC signature
- IP allowlisting (only Wazuh manager can reach the webhook)
- Rate limiting / basic abuse protection

## Shuffle → TheHive (Case creation / updates)
**Goal:** Create and update cases based on alert context and severity.
- Shuffle creates TheHive cases via API and attaches key observables and metadata.
- Case formatting is standardized (title, severity, tags) to support consistent triage.

**Recommended mapping (example)**
- Title: `[{severity}] {rule.description} on {agent.name}`
- Severity mapping (rule.level → severity):
  - **Low:** 0–7
  - **Medium:** 8–12
  - **High:** 13–16
- Observables: `srcip`, `user`, `url`, `process`, `host`, etc.
- Attach raw log: `full_log`

## TheHive → Cortex (Automated analysis)
**Goal:** Enrich observables (IP/domain/URL/hash) via analyzers.
- TheHive triggers Cortex analyzers based on incident type.
- Cortex returns enrichment reports to the case for analyst review.

**Configured analyzers (examples)**
- VirusTotal
- Shodan
- DomainTools

## MISP → Wazuh & TheHive (IOC enrichment)
**Goal:** Correlate alerts and cases against threat intelligence.
- MISP ingests IOCs from feeds and curated events.
- Wazuh correlates events against IOCs for detection context.
- TheHive attaches IOC context to cases when relevant.

## Shuffle → Notifications / Response
- Notifications: **Discord** and **Slack**
- Response: **auto-block malicious IPs** on the firewall (via a dedicated Shuffle workflow)
