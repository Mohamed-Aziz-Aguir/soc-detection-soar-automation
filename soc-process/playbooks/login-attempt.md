# Playbook — AD Login Attempts (Threshold Lockout)

## Incident type
Repeated authentication failures against Active Directory accounts.

## Trigger
Wazuh detection / correlation for multiple failed logons (e.g., 3 failures in 3 minutes).

## Automated actions (Shuffle)
1. Receive Wazuh alert via webhook
2. Parse user + source information (username, srcip/workstation if available)
3. **Active Directory**: lock/disable account according to threshold policy
4. **TheHive**: create alert → create case
5. Optional enrichment via Cortex (IP/domain context)
6. Notify SOC via Discord/Slack

## Analyst SOP (Tier 1)
1. Validate legitimacy (user forgot password vs attack):
   - Check whether the user reported issues
   - Review source workstation and location
2. Confirm lockout action was correct and scoped
3. Identify if attempts are distributed (password spray) or single source (guessing)
4. Add case notes and assign to Tier 2 if suspicious

## Escalation criteria (Tier 2)
- Multiple accounts affected (password spray)
- Same source attempting many users
- Evidence of successful login after failures
- Privileged/VIP account targeted

## Closure criteria
- Root cause determined (benign vs malicious)
- Account unlocked only after validation and guidance to user/IT
