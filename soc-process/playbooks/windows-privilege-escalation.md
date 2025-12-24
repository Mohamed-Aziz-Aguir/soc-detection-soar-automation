# Playbook — Windows Privilege Escalation

## Incident type
Suspicious Windows privilege escalation attempt (local admin/system-level elevation signals).

## Trigger
Wazuh detection for Windows privilege escalation (rule-based).

## Automated actions (Shuffle)
1. Receive Wazuh alert via webhook
2. Parse/normalize key fields (user, host, rule, severity)
3. **TheHive**: create alert → create case
4. **Active Directory**: get user attributes (context)
5. **Active Directory**: lock/disable user (containment)
6. Notify SOC via **Discord** (and optionally Slack)

## Analyst SOP (Tier 1)
1. Validate the alert:
   - Confirm host and user identity
   - Confirm whether activity is expected (maintenance/admin tasks)
2. Review user and host context:
   - Recent logons, group memberships, privileged roles
3. Confirm containment:
   - Account locked/disabled as expected
4. Collect supporting evidence:
   - Event timeline around escalation, relevant Windows logs/Sysmon if available
5. Record disposition in TheHive:
   - True positive / false positive / needs more data

## Escalation criteria (Tier 2)
Escalate if any of the following:
- Privileged account compromise suspected
- Multiple hosts affected
- Signs of credential dumping or lateral movement
- Persistence mechanisms suspected

## Closure criteria
- Root cause identified or ruled out
- Account status returned to normal (if false positive) with documented justification
- Post-incident tuning action created (if needed)
