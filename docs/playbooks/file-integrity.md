# Playbook — File Integrity Monitoring (Create/Modify/Delete)

## Incident type
Unauthorized file change detection (create/modify/delete), potentially indicating persistence, tampering, or cleanup.

## Trigger
Wazuh FIM alert.

## Automated actions (Shuffle)
1. Receive Wazuh alert via webhook
2. Parse fields (file path, action type, hashes, host/user)
3. Optional containment:
   - **Velociraptor** quarantine for critical paths (policy-based)
4. **TheHive**: create alert
5. Branch by action type:
   - **Modify**: create case for modify
   - **Add/Delete**: create case for add/delete
6. Add hash observables (before/after where available: MD5/SHA1/SHA256)
7. **Cortex**: run hash analyzers (VirusTotal, etc., depending on configuration)
8. Merge results
9. Notify SOC via Discord (and optionally Slack)

## Analyst SOP (Tier 1)
1. Validate file context:
   - File path criticality (system32, startup, webroot, SSH keys, scripts)
2. Review hashes and analyzer results:
   - Known malware?
   - Unknown → escalate for deeper analysis
3. Correlate with other telemetry:
   - Who/what modified the file?
   - Any related auth/privilege escalation alerts?
4. Decide response:
   - Restore from known-good
   - Remove malicious file
   - Keep for forensics
5. Document actions and evidence in TheHive

## Escalation criteria (Tier 2)
- Change in critical OS/security configuration files
- Malicious hash confirmation
- Repeated tampering on same host
- Suspicious parent process / privilege escalation correlation

## Closure criteria
- File integrity restored or change authorized and documented
- Case notes include hash outcomes, decision, and remediation
