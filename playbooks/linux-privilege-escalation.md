# Playbook — Linux Privilege Escalation

## Incident type
Suspected Linux privilege escalation / unauthorized privileged command execution.

## Trigger
Wazuh detection of privilege escalation activity (e.g., sudo abuse or related signals).

## Automated actions (Shuffle)
1. Receive Wazuh alert via webhook
2. Parse/normalize fields (user, host, command/context)
3. **Velociraptor**: quarantine/isolate endpoint (containment)
4. **TheHive**: create alert → create case
5. Add observables (user/host/srcip/command as available)
6. Notify SOC (Discord/Slack)

## Analyst SOP (Tier 1)
1. Validate detection context:
   - Which user executed the action?
   - Which host/zone?
2. Verify containment:
   - Confirm Velociraptor quarantine succeeded
3. Triage the activity:
   - Was this expected admin behavior?
   - Check change window / authorized maintenance
4. Evidence collection (Tier 2 if needed):
   - Pull process list, login history, shell history, auth logs
5. Document outcome and next steps in TheHive

## Escalation criteria (Tier 2)
- Unknown user performing privileged actions
- Command patterns match known malicious behavior
- Multiple privilege escalation alerts on same host
- Any sign of persistence/backdoor

## Closure criteria
- Host verified clean or reimaged
- Authorization verified (if legitimate)
- Tuning ticket created (if false positive)
