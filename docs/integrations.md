# Integrations

## Wazuh → Shuffle (Webhook ingestion)
- Wazuh forwards alerts to Shuffle using a webhook integration.
- Shuffle performs parsing/normalization, routing, and conditional handling (including dedupe for selected workflows).

## Shuffle → TheHive (Alert → Case)
- Shuffle creates a TheHive Alert first.
- Alert is promoted to a Case when workflow conditions match (e.g., threshold, high-confidence category, IOC match).

## TheHive → Cortex (Enrichment)
- Enrichment occurs after case creation.
- Analyzers used: VirusTotal, Shodan, DomainTools.

## MISP IOC correlation
IOC types used:
- domain / URL / hash / srcip

IOC matches can increase confidence/severity and trigger additional response actions.

## Notifications
- Discord + Slack

## Response integrations (conditional)
- pfSense: IP blocking / network enforcement
- Active Directory: user lock/disable and logoff actions (scenario-dependent)
- Velociraptor: endpoint quarantine/containment (scenario-dependent)

For **sudo executed** incidents, the response path applies **both**: Active Directory action and Velociraptor quarantine.
