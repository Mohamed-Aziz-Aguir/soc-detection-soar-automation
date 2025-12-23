# Playbook — SSH Brute Force (SSH login failed)

## Incident type
SSH brute-force attempts against a Linux/Unix SSH service.

## Trigger
Wazuh detection of repeated SSH authentication failures (thresholded / correlated).

## Automated actions (Shuffle)
1. Receive Wazuh alert via webhook
2. Parse fields (src IP, agent/host, rule, timestamps)
3. **pfSense**: add block rule for attacker IP (WAN/edge)
4. **TheHive**: create alert → create case
5. **Cortex**: enrich attacker IP (reputation/WHOIS/OSINT depending on analyzers)
6. Notify SOC via **Discord** (and optionally Slack)

## Analyst SOP (Tier 1)
1. Open TheHive case and verify:
   - Target host/service
   - Source IP details (internal vs external)
   - Frequency and timeframe
2. Validate containment:
   - Confirm pfSense rule exists and is correctly scoped
3. Review enrichment results:
   - Reputation score, ASN/geo, previous sightings
4. Check for follow-on activity:
   - Any successful SSH logins?
   - Any lateral movement indicators?
5. Document outcome:
   - Add a case note: “Blocked at pfSense; no successful login observed”

## Escalation criteria (Tier 2)
Escalate if any of the following:
- Successful authentication observed
- Same attacker IP targets multiple critical assets
- Internal source IP (possible compromised internal host)
- Evidence of persistence or privilege escalation

## Closure criteria
- Block applied and verified
- No successful login or post-compromise activity observed in the time window
- Case notes updated with evidence
