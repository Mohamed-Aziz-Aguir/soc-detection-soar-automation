# Metrics & SOC KPIs

SOC Operations Center includes a metrics-oriented SOC dashboard (mock-up) intended to present:
- Alert volume and trends
- Workflow executions
- Case counts
- MTTR proxy (average response time)
- Tool health and connectivity

## Recommended metric definitions
- **MTTD (proxy):** event timestamp → case creation
- **MTTR (proxy):** case creation → contained/closed
- **Automation coverage:** % of incidents where enrichment/notification executed automatically
- **Noise ratio:** alerts per confirmed incident (manual sampling)
