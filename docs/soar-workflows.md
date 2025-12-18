# SOAR Workflows (Shuffle)

## Standard behavior (project-wide)
- Create TheHive **Alert**, then promote to **Case** (Alert → Case) based on decision logic.
- Enrich after case creation using Cortex analyzers (VirusTotal, Shodan, DomainTools) when applicable.
- Notify Discord and Slack.
- Conditional response: pfSense block / AD action / Velociraptor quarantine depending on trigger.
- Deduplication is implemented in some workflows using a guard step (keyed by `rule.id + srcip + agent.name`).

## Workflow catalog
| File | Purpose |
|---|---|
| `ssh_login_failed.json` | SSH brute-force / auth failures |
| `login_attempt.json` | Login attempt routing |
| `sudo_executed.json` | Linux privilege escalation indicator |
| `windows_privilege_activity.json` | Windows privilege activity |
| `file_integrity.json` | File integrity events |
| `cipher_execution.json` | cipher.exe execution |

## Per-workflow template (use for precision)
### Workflow: {{NAME}}
- Trigger rule(s): {{Wazuh rule IDs}}
- Dedupe: {{yes/no}} — key `rule.id + srcip + agent.name`
- Case policy: Alert only vs promote to Case
- Enrichment: which analyzers and under what condition
- Response: pfSense/AD/Velociraptor conditions
- Analyst workflow: what the ticket requires to validate/rollback
