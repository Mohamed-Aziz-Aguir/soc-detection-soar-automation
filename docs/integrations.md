# Integrations

## Wazuh → Shuffle (Webhook)
### Purpose
Forward selected Wazuh alerts to Shuffle for orchestration.

### Implementation outline
1. Configure Wazuh integration to POST alerts to a Shuffle webhook URL.
2. Standardize the alert payload fields used by workflows.
3. Validate webhook authenticity (recommended: secret header/HMAC).

### Payload expectations (example)
- `rule.id`, `rule.level`, `rule.description`
- `agent.id`, `agent.name`, `agent.ip`
- `data.srcip`, `data.user`, `full_log` (as available)

## Shuffle → Downstream Actions
Document each downstream action (case creation, ticketing, notifications), including:
- Endpoint URL and auth method (token, basic, etc.)
- Required permissions
- Error handling & retries
