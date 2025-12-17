# Incident Response Process

## Goal
Turn detections into consistent incident handling outcomes with clear analyst steps and audit-ready records.

## Lifecycle (aligned with common IR practice)
1. Identification (Wazuh alert)
2. Triage (validate signal, assign severity, determine scope)
3. Investigation (confirm indicators, collect evidence)
4. Containment (controlled actions; analyst approval recommended)
5. Eradication & Recovery
6. Lessons learned (tuning + playbook updates)

## Case template (recommended fields)
- Title: `[{severity}] {rule.description} on {agent.name}`
- Severity: Low / Medium / High
- Observables: IP, user, host, URL, hash, command (as available)
- Tasks:
  1. Validate detection context
  2. Scope impacted entities
  3. Enrich observables (Cortex/MISP)
  4. Decide containment
  5. Document outcome and improvements

## Automation boundaries
- Automate repetitive steps (case creation, enrichment, notifications)
- Keep destructive actions (blocking, account disable) behind a control/approval step unless safely scoped
