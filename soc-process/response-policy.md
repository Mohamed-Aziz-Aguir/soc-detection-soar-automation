# Response Policy (Automation Gates + Scenario Mapping)

This policy defines when response actions run automatically vs requiring analyst confirmation.  
It also documents the **scenario-by-scenario** behavior implemented in this project.

## Automation gates

### Auto (no approval)
Used when:
- High/Critical severity and strong confidence (e.g., brute-force from external IPs)
- Confirmed IOC matches (MISP/Cortex) for high-risk artifacts
- Low business impact enforcement actions (e.g., edge firewall block)

Actions may include:
- pfSense block
- AD lock/disable (policy-dependent)
- Velociraptor quarantine

### Semi‑Auto (approval gate)
Used when:
- High business impact actions (service/VIP accounts, critical servers)
- Signal confidence is medium or context-dependent

Pattern:
- Prepare action + notify analyst
- Execute upon approval

### Manual
Used when:
- Business validation is required
- Investigation is needed before enforcement

Pattern:
- Case creation + enrichment + analyst guidance

---

## Implemented scenario mapping


# Response Policy (Scenario Mapping)

Rollback/removal was performed manually during testing to simulate ticket-driven operations and analyst verification.

## File integrity changes (add/modify/delete)
- Action: Create Alert → Case
- Notify: Discord (immediate awareness)
- Response: no automatic enforcement; analyst decides next actions

## sudo executed (privilege activity)
- Action: Create Alert → Case
- Response: Endpoint containment via Velociraptor quarantine and Active Directory action (always (both actions))

## cipher.exe execution
- Action: Create Alert → Case
- Response:
  - Block source IP (pfSense)
  - Lock down the endpoint (Velociraptor containment)

## Login attempts failed (AD)
- Condition: 3 failures within 3 minutes
- Response: Active Directory block/lock action

## SSH login failures / brute force
- Action: Create Alert → Case
- Enrichment: Cortex scan/enrichment of source IP
- Response: pfSense block

## PowerShell encoded command
- Response:
  - Force logoff (Active Directory)
  - Lock down endpoint (Active Directory containment policy)
