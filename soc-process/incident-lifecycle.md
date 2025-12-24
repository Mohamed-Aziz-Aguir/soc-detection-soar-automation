# Incident Lifecycle (Project Model)

This project uses a case-management lifecycle aligned with common SOC practice.

## States
1. **New**
2. **Triage**
3. **Investigating**
4. **Containment**
5. **Eradication**
6. **Recovery**
7. **Closed**

## Required case fields (recommended)
- Alert source (rule id, agent, timestamp)
- Observables (srcip, domain/url/hash, username, hostname)
- Actions taken (who/what/when)
- Disposition (TP/FP/Benign)
- Lessons learned / tuning ticket

---

## TheHive Case States Used (Project)

States used:
- New
- Triage
- Investigating
- Assigned (assigned to an analyst)
- Closed

Automation behavior:
- Some incidents can be auto-resolved and set to Closed.
- Otherwise, cases are created in New and progress through triage/investigation with analyst assignment.
