# Playbook — cipher.exe Execution (Ransomware-like Indicator)

## Incident type
Potential ransomware / destructive action indicator (cipher.exe execution).

## Trigger
Wazuh detection of `cipher.exe` execution on a Windows endpoint.

## Automated actions (Shuffle)
1. Receive Wazuh alert via webhook (cipher event)
2. Optional delay node (stabilize collection / avoid duplicates)
3. **Active Directory**: disconnect/disable user (containment)
4. **TheHive**: create alert → create case
5. Add observables (IP/host/user as available)
6. **Cortex**: run IP analyzers (and hash analyzers if present)
7. Merge enrichment results
8. Notify SOC via Discord (and optionally Slack)

## Analyst SOP (Tier 1)
1. Confirm process execution details:
   - Path, parent process, user context
2. Check for impact evidence:
   - File encryption activity, suspicious file modifications, shadow copy deletion
3. Validate containment:
   - Account disabled and endpoint isolated if required
4. Review enrichment:
   - Any known bad indicators?
5. Escalate if impact is confirmed or spreading is suspected

## Escalation criteria (Tier 2/IR)
- Evidence of encryption or destructive activity
- Multiple hosts affected
- Suspected lateral movement
- Known ransomware IOCs confirmed by enrichment

## Closure criteria
- Endpoint contained and assessed
- Scope confirmed (single host vs multiple)
- Recovery/remediation completed and documented
