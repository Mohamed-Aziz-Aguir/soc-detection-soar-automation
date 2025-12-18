# Integrations

## Wazuh → Shuffle (Webhook ingestion)
- Wazuh forwards alerts to Shuffle using a webhook integration.
- Shuffle parses fields for routing and observables (e.g., `rule.*`, `agent.*`, `data.srcip`, `data.user`, `full_log`).

## Shuffle → TheHive (Alert → Case)
- Shuffle creates a TheHive **Alert** first.
- For medium/high severity and/or IOC matches, the Alert is promoted to a **Case** and enriched with tasks/observables.

## TheHive → Cortex (Enrichment)
Analyzers used:
- VirusTotal
- Shodan
- DomainTools

Enrichment is performed **after** case creation.

## MISP ↔ Wazuh / TheHive (Threat intelligence)
- IOC matches can increase confidence/severity and trigger additional response steps.

## Shuffle → Notifications
- Discord + Slack are used as SOC channels for notifications and escalation.

## Shuffle → Response actions (policy)
Response actions are considered when one or more conditions are met:
- High severity threshold: `rule.level >= 13`
- IOC match via MISP correlation
- Trigger category (e.g., brute force / privilege activity / suspicious PowerShell)

Rollback during testing is manual to simulate a ticket-driven SOC workflow where an analyst validates and reverses actions if needed.
