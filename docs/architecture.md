# Architecture

## High-level flow
1. **Telemetry & Detection**: Wazuh ingests logs and evaluates custom rules.
2. **Alert Forwarding**: Wazuh triggers a webhook on matching alerts.
3. **SOAR Orchestration**: Shuffle receives the webhook, normalizes data, enriches context, and decides actions.
4. **Case/Ticketing**: Shuffle creates a case/ticket and attaches key observables.
5. **Notifications**: Shuffle alerts stakeholders (email/chat) and logs outcomes for auditability.

## Components
- **Wazuh**: SIEM/detection, alerting via webhook
- **Shuffle**: SOAR workflows for routing, enrichment, ticketing, and notifications
- **(Optional)** TheHive/Cortex/MISP: case mgmt + enrichment (documented if used)
- **(Optional)** Suricata/pfSense: network telemetry sources

## Data contracts
Define the webhook payload schema and required fields (e.g., rule.id, rule.level, agent.name, srcip, user, etc.).

## Security considerations
- Webhook authentication (shared secret/HMAC) and IP allowlisting
- Least-privilege API keys for any downstream systems
- Secret management (no tokens in repo)
