# File Integrity Monitoring Workflow

## Trigger
- Wazuh FIM alerts (create/modify/delete)

## Flow
1. Webhook trigger
2. Quarantine (Velociraptor)
3. Create alert
4. Branch:
   - Modification: Create case for modify
   - Creation/Deletion: Create case add/delete
5. Add hash observables (before/after)
6. Run hash analyzers
7. Merge case
8. Discord notification

## Purpose
Detect unauthorized file changes and validate integrity.
