# Cipher.exe Execution Workflow

## Trigger
- Wazuh rule detecting cipher.exe execution

## Flow
1. Webhook trigger
2. Delay node
3. Active Directory: Disable machine/user
4. TheHive: Create alert
5. Create case
6. Add IP observable
7. Run IP analyzers
8. Merge results
9. Discord notification
10. Close case manually

## Purpose
Detect ransomware-like activity and isolate affected systems.
