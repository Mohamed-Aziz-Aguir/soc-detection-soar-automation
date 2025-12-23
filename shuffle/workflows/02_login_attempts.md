# Login Attempt Workflow

## Trigger
- Wazuh Webhook (failed logins)

## Flow
1. Receive login attempt alert
2. Create alert in TheHive
3. Create case
4. Add observable (user/IP)
5. List Cortex analyzers
6. Run analyzers
7. Lock AD account if threshold exceeded
8. Discord notification
9. Close case if automated

## Purpose
Protect Active Directory accounts from brute-force attempts.
