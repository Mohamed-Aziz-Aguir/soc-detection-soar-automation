# Incident Response Process

CyberSentinels follows a practical SOC lifecycle aligned with common IR practice.

## Lifecycle
1. Identification (Wazuh alert)
2. Triage (severity, scope, confidence)
3. Investigation (evidence collection, enrichment)
4. Containment / Response (conditional automation + analyst oversight)
5. Recovery
6. Lessons learned (tuning + workflow adjustments)

## Automation boundaries
- Repetitive tasks (case creation, enrichment, notifications) are automated.
- High-impact response actions (blocking/quarantine/identity actions) are triggered conditionally and were rolled back manually during testing to simulate a ticket-driven SOC workflow.
