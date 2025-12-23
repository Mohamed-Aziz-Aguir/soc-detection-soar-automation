# SSH Login Failed Workflow

## Trigger
- SSH authentication failures

## Flow
1. Webhook trigger
2. Parser extracts IP
3. pfSense: Block source IP
4. Create alert
5. Create case
6. Add IP observable
7. Run IP analyzers
8. Discord alert
9. Close case

## Purpose
Stop SSH brute-force attacks automatically.
