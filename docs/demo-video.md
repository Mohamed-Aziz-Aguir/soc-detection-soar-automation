# Demo Video (CyberSentinels)

- YouTube: https://www.youtube.com/watch?v=DYTV5zdeY8U

## Purpose of the demo
The demo is intended to explain:
- **Who we are:** CyberSentinels (a SOC initiative / project)
- **What the application is:** a SOC platform integrating detection, orchestration, case management, enrichment, threat intel, and response
- **How an incident flows end-to-end:** Wazuh → Shuffle → TheHive (Alert→Case) → Cortex + notifications + response

## Suggested talk track (keep it concise)
1. Introduction: CyberSentinels mission and scope
2. Architecture overview (use `docs/diagrams/architecture.png`)
3. Walkthrough of the SOC operations UI (mock-up screenshots in `assets/screenshots/`)
4. Demonstrate one incident scenario and show:
   - Wazuh alert
   - Shuffle decisioning (severity + dedupe + IOC checks)
   - TheHive alert and case creation
   - Cortex enrichment (VirusTotal/Shodan/DomainTools)
   - Discord/Slack notification
   - Response action (pfSense/AD/Velociraptor) when applicable
5. Close: what this reduces (manual triage) + what it proves (SOC engineering)

## Timestamp slots (fill in)
- 00:00 — Intro
- 00:__ — Architecture
- 00:__ — UI walkthrough
- 00:__ — Incident scenario
- 00:__ — Enrichment + response
- 00:__ — Summary
