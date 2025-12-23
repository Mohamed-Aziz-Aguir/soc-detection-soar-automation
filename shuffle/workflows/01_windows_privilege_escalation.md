# Windows Privilege Escalation Workflow

## Trigger
- **Source**: Wazuh Webhook
- **Condition**: Windows privilege escalation detection

## Flow
1. Webhook receives alert
2. Shuffle parser normalizes fields
3. TheHive: Create alert
4. TheHive: Create case
5. Active Directory: Get user attributes
6. Active Directory: Lock user
7. Discord: Notify SOC

## Purpose
Immediate containment of suspected Windows privilege escalation by disabling account access and alerting SOC.
