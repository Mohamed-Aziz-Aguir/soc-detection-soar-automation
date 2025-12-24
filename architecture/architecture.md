# Architecture

## Core data flow

1. Wazuh → Shuffle: Wazuh forwards selected alerts to Shuffle via webhook.
2. Shuffle → TheHive: Shuffle creates a TheHive Alert, then promotes it to a Case (Alert → Case) based on workflow logic.
3. TheHive → Cortex: Cortex analyzers enrich observables and attach results to the case.
4. MISP ↔ Wazuh/TheHive: IOC correlation enriches alerts/cases and influences response decisions.
5. Shuffle → Notifications: Discord + Slack.
6. Shuffle → Response (conditional): pfSense block, Active Directory action, and/or Velociraptor endpoint containment depending on trigger.

## Severity mapping (Wazuh rule.level)

* Low: 0–7
* Medium: 8–12
* High: 13–16

## Deduplication (partial)

Not all workflows implement dedupe. Where implemented, it uses:

* rule.id + srcip + agent.name
