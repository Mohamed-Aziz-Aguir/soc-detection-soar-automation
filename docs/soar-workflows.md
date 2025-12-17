# SOAR Workflows (Shuffle)

This section documents workflow behavior, inputs, decision logic, and actions.

## Operational defaults
- Severity mapping: Low 0–7, Medium 8–12, High 13–16
- Deduplication key: `rule.id + srcip + agent.name`
- Notifications: Discord + Slack
- Case handling: TheHive Alert → Case
- Enrichment: Cortex analyzers (VirusTotal, Shodan, DomainTools)

## Workflow catalog
| File | Purpose | Primary actions |
|---|---|---|
| `ssh_login_failed.json` | SSH failures / brute-force | Alert→Case + notify + optional block |
| `login_attempt.json` | Login attempts | Alert + notify + routing |
| `sudo_executed.json` | Privilege escalation indicators | Case + enrichment + notify |
| `windows_privilege_activity.json` | Windows privilege activity | Case + tasks + notify |
| `file_integrity.json` | File integrity events (add/modify/delete) | Alert→Case + notify |
| `work_cipher.json` | cipher.exe execution | Alert→Case + notify + optional block |

## Workflow specification template (use per workflow)
### Workflow: {{NAME}}
- **Trigger:** Wazuh webhook
- **Inputs:** rule.id, rule.level, agent.name, srcip (if present), full_log
- **Dedupe:** `rule.id + srcip + agent.name`
- **Decisioning:** severity mapping + IOC match checks + high-severity thresholds
- **Actions:** TheHive Alert → Case, Cortex analyzers (if applicable), Discord/Slack notify, optional response (pfSense/AD/Velociraptor)
- **Rollback:** manual unblock/quarantine removal during testing
