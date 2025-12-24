# Shuffle Workflow — Windows Privilege Escalation

## Purpose
Automate alert-to-case handling and response actions for **Windows Privilege Escalation**, including enrichment and SOC notifications.

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
1. Webhook receives alert
2. Shuffle parser normalizes fields
3. TheHive: Create alert
4. TheHive: Create case
5. Active Directory: Get user attributes
6. Active Directory: Lock user
7. Discord: Notify SOC

## Actions
- Case management: TheHive alert → case
- Enrichment: Cortex analyzers (VirusTotal, Shodan, DomainTools as configured)
- Response: pfSense block / AD lock / Velociraptor quarantine depending on scenario
- Notifications: Discord + Slack

## References
- ATT&CK techniques: T1068
- Workflow export (sanitized): `../exports/windows-privilege-escalation.json`
- Analyst playbook (SOP): `../../soc-process/playbooks/windows-privilege-escalation.md`
