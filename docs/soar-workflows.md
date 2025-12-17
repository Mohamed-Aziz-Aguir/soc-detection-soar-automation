# SOAR Workflows (Shuffle)

## Content type (what to document)
Each workflow is documented as a **Workflow Spec + Operational Runbook**:
- Trigger
- Inputs (required fields)
- Normalization & parsing
- Decisioning (severity mapping, routing, dedupe)
- Actions (case/ticketing, enrichment, notifications, response)
- Outputs (case ID, message ID)
- Failure handling
- Security controls
- Testing/validation

## Operational defaults used
- Severity mapping (Wazuh `rule.level` → severity):
  - **Low:** 0–7
  - **Medium:** 8–12
  - **High:** 13–16
- Notifications: **Discord** and **Slack**
- Deduplication: implemented via **counter/guard script** inside workflows to prevent duplicate executions for the same recurring attack pattern

## Workflow catalog (from exports)
| Workflow file | Intended use | Trigger | Primary actions | Notes |
|---|---|---|---|---|
| `workflows/shuffle/ssh_login_failed.json` | SSH failures / brute force | Wazuh webhook | Notify + case creation/update | {{fill}} |
| `workflows/shuffle/sudo_executed.json` | Privilege escalation indicators | Wazuh webhook | Case + enrichment + notify | {{fill}} |
| `workflows/shuffle/login_attempt.json` | Login attempts | Wazuh webhook | Routing + notify | {{fill}} |
| `workflows/shuffle/file_integrity.json` | File integrity events | Wazuh webhook | Case + notify | {{fill}} |
| `workflows/shuffle/work_cipher.json` | TLS/cipher/security event | Wazuh webhook | Enrich + notify | {{fill}} |
| `workflows/shuffle/workflow_saif_priv_windows.json` | Windows privilege activity | Wazuh webhook | Case + tasks | {{fill}} |
| `workflows/shuffle/unlock.json` | Account unlock / auth event | Wazuh webhook | Notify + case update | {{fill}} |

---

## Template (duplicate this section per workflow)
### Workflow: {{WORKFLOW_NAME}}
- **File:** `workflows/shuffle/{{FILE_NAME}}`
- **Purpose:** {{one sentence}}
- **Trigger:** Wazuh webhook
- **Owned detections:** {{Wazuh rule IDs / groups}}

#### Inputs (required)
- `rule.id`, `rule.level`, `rule.description`
- `agent.name`, `agent.id`, `agent.ip`
- `timestamp` or unique `alert.id`
- Event-specific: {{data.srcip, data.user, etc.}}

#### Decisioning
- **Severity mapping:** Low 0–7, Medium 8–12, High 13–16 (based on Wazuh `rule.level`)
- **Deduplication:** Implemented using a counter/guard script to prevent duplicate executions/notifications for the same recurring attack pattern (same trigger + same key fields).
- **Routing:** {{conditions for case creation vs notify-only}}

#### Actions
1. Create/update TheHive case
2. Add observables/tags
3. Trigger Cortex analyzers (when applicable): VirusTotal, Shodan, DomainTools
4. Notify (Discord + Slack)
5. Automated response (when applicable): firewall auto-block of malicious IPs

#### Failure handling
- Retries: {{count/backoff}}
- Fallback: send Discord/Slack notification with raw payload and record failure

#### Security
- Webhook auth: shared secret header (recommended) and/or HMAC signature
- Secrets storage: Shuffle secrets/env vars
- Least privilege tokens

#### Testing
- How you validated this workflow: {{manual test payload / replay / live alert}}
