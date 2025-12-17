# Integrations

This section documents how the platform components exchange signals and context.

## Wazuh → Shuffle (Webhook ingestion)
- Wazuh forwards selected alerts to Shuffle via webhook.
- Shuffle parses fields used for routing and observables (e.g., `rule.*`, `agent.*`, `data.srcip`, `data.user`, `full_log`).

## Shuffle → TheHive (Alert → Case)
- Shuffle creates a TheHive **Alert** and attaches extracted observables.
- For higher-confidence events, the Alert is promoted to a **Case** (or Case is created) with tasks and severity applied.

## TheHive → Cortex (Enrichment)
- Cortex analyzers are triggered from TheHive based on observable type and incident category.
- Analyzers used: **VirusTotal**, **Shodan**, **DomainTools**.

## MISP ↔ Wazuh / TheHive (Threat intelligence)
- MISP provides IOC context used to enrich Wazuh detections and TheHive cases.
- IOC matches can influence severity and response decisions (e.g., blocking).

## Shuffle → Notifications (Discord + Slack)
- Notifications are posted to Discord and Slack with key incident context and case references.

## Shuffle → Response actions (conditional)
Response depends on trigger category and context:
- **High-severity threshold** handling
- **IOC matches** (MISP correlation)
- Enforcement paths: **pfSense block**, **Active Directory actions**, **Velociraptor quarantine**
Rollback for testing was performed manually to simulate real ticket-driven operations.
