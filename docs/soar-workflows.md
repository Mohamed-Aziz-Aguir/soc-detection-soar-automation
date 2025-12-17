# SOAR Workflows (Shuffle) — CyberSentinels

## Documentation standard
For each workflow, document:
- Trigger and input fields
- Decisioning (severity mapping + dedupe)
- Actions (TheHive case ops, Cortex analyzers, notifications, firewall block)
- Failure handling and security controls

## Operational defaults
- Severity mapping: Low 0–7, Medium 8–12, High 13–16
- Notifications: Discord + Slack
- Deduplication: counter/guard step to avoid duplicate notifications for the same recurring attack pattern

## Workflow exports
See `workflows/shuffle/`.

## Per-workflow template (fill for each workflow)
### Workflow: {{WORKFLOW_NAME}}
- **File:** `workflows/shuffle/{{FILE_NAME}}`
- **Purpose:** {{one sentence}}
- **Trigger:** Wazuh webhook
- **Wazuh rule(s):** {{rule ids}}

#### Observables extracted
- IP: {{srcip/dstip}}
- User: {{user}}
- Host: {{agent.name}}
- Command/Process: {{command/process}}
- URL/Domain: {{url/domain}}

#### Actions
1. Create/update TheHive case
2. Add observables and tags
3. Trigger Cortex analyzers (VirusTotal / Shodan / DomainTools) when applicable
4. Notify Discord + Slack
5. Auto-block IP workflow (only when conditions match)

#### Dedupe key (slot)
- Dedupe key fields: {{e.g., rule.id + agent.name + srcip + 10m window}}

#### Error handling
- Retries: {{count/backoff}}
- Fallback: notify SOC channel with failure context
