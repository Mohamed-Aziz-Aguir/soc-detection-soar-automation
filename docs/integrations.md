# Integrations (CyberSentinels)

This repo documents integration logic without exposing secrets.

## Wazuh → Shuffle (Webhook)
- **Purpose:** forward selected alerts for orchestration.
- **Typical payload fields used:** `rule.id`, `rule.level`, `rule.description`, `agent.name`, `agent.ip`, `full_log` plus event-specific fields.

## Shuffle → TheHive (Case Management)
- **Purpose:** create/update cases and attach observables.
- **Case formatting:** standardized title + severity + tags/observables.
- **Severity mapping:** Low 0–7, Medium 8–12, High 13–16.

## TheHive → Cortex (Enrichment)
- **Purpose:** execute analyzers and attach reports to cases.
- **Analyzers used (examples):** VirusTotal, Shodan, DomainTools.

## MISP → Wazuh & TheHive (Threat Intel)
- **Purpose:** IOC correlation and enrichment for alerts/cases.

## Shuffle → Discord & Slack (Notifications)
- **Purpose:** real-time analyst notifications and escalation.

## Shuffle → Firewall (Automated Response)
- **Purpose:** auto-block malicious IPs via a dedicated Shuffle workflow.
- **Control recommendation:** keep an allowlist/denylist and document rollback steps.
