# Shuffle Workflow — AD Login Attempt Threshold / Lockout

## Purpose
Automate alert-to-case handling and response actions for **AD Login Attempt Threshold / Lockout**, including enrichment and SOC notifications.

## Trigger
- Wazuh webhook payload (rule hit / correlation)

## Inputs (expected fields)
- `rule.id`, `rule.level`, `agent.name`
- `data.srcip` (when applicable)
- `data.user` / `win.eventdata.SubjectUserName` (when applicable)
- Observables: `srcip`, `domain`, `url`, `hash` (depending on detection)

## Processing & decision points
- Deduplication: suppress repeated identical alerts where configured (count/window logic)
- Severity gating: 0–7 low, 8–12 medium, 13–16 high (see `soc-process/severity-model.md`)
- Action gating: auto vs semi-auto vs manual (see `soc-process/response-policy.md`)

## Execution order (as implemented)
1. Receive login attempt alert
2. Create alert in TheHive
3. Create case
4. Add observable (user/IP)
5. List Cortex analyzers
6. Run analyzers
7. Lock AD account if threshold exceeded
8. Discord notification
9. Close case if automated

## Actions
- Case management: TheHive alert → case
- Enrichment: Cortex analyzers (VirusTotal, Shodan, DomainTools as configured)
- Response: pfSense block / AD lock / Velociraptor quarantine depending on scenario
- Notifications: Discord + Slack

## References
- ATT&CK techniques: T1110.001
- Workflow export (sanitized): `../exports/login-attempt.json`
- Analyst playbook (SOP): `../../soc-process/playbooks/login-attempt.md`
