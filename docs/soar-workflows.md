# SOAR Workflows (Shuffle)

For each workflow export:
- **Trigger**: webhook / schedule / manual
- **Input schema**: required fields
- **Decision logic**: severity mapping, deduping, routing rules
- **Actions**: create case/ticket, enrich, notify, collect evidence
- **Failure modes**: what happens if downstream systems fail
- **Security**: secrets handling and least privilege

## Workflow catalog
Add a table:
| Workflow | Trigger | Primary action | Notes |
|---|---|---|---|
