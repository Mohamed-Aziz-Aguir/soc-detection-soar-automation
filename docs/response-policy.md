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
