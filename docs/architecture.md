# Architecture

## Core data flow
1. **Wazuh → Shuffle:** Wazuh forwards selected alerts to Shuffle via a webhook.
2. **Shuffle → TheHive:** Shuffle creates a TheHive **Alert**, then promotes it to a **Case** (Alert → Case) based on decision logic.
3. **TheHive → Cortex:** Cortex analyzers enrich case observables. Results are attached back to the case.
4. **MISP ↔ Wazuh/TheHive:** IOC correlation enriches alerts and influences severity and response.
5. **Shuffle → Notifications:** Discord and Slack notifications are sent for analyst awareness.
6. **Shuffle → Response (conditional):**
   - pfSense IP block
   - Active Directory actions (when applicable)
   - Velociraptor quarantine/response (when applicable)

## Severity mapping (Wazuh `rule.level`)
- Low: 0–7
- Medium: 8–12
- High: 13–16

## Deduplication (where implemented)
Some workflows include a guard/counter step to avoid duplicate actions for recurring events using:
- `rule.id + srcip + agent.name`

## Diagrams
Add your diagrams here:
- `docs/diagrams/architecture.png`
- `docs/diagrams/network-zones.png`
- `docs/diagrams/workflow-sequence.png`
