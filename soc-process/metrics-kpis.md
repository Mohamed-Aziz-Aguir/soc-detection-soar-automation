# Metrics & SOC KPIs

Metrics in SOC Operations Center are real and pulled from tool APIs (as used in the project).

Examples shown in the operations UI:
- Uptime/health per tool
- Alert volume and case volume
- Workflow executions
- High-level response time metrics (MTTR proxy)

Recommended definitions:
- MTTD (proxy): event timestamp → case creation
- MTTR (proxy): case creation → closed/contained
- Automation coverage: % incidents where enrichment/notifications executed automatically

---

## Minimal KPI Set (Summary)

# Metrics & KPIs

Track:
- MTTD / MTTA / MTTR
- Cases by severity
- Automation rate
- False positive rate (requires disposition tracking)
