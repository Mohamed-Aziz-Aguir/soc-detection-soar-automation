# Architecture

## Overview
CyberSentinels implements an end-to-end SOC pipeline where detections are converted into actionable incident handling using automation and enrichment.

### Core flow
1. **Wazuh → Shuffle**: Wazuh sends alerts to Shuffle via webhook.
2. **Shuffle → TheHive**: Shuffle creates TheHive **Alerts**, then promotes/creates **Cases** (Alert → Case).
3. **TheHive → Cortex**: Cortex analyzers are triggered to enrich observables; results are attached back to the case.
4. **MISP → Wazuh/TheHive**: IOC correlation enriches detections and cases.
5. **Shuffle → Notifications**: Discord and Slack notifications for SOC awareness and escalation.
6. **Shuffle → Response**: Conditional response actions based on trigger context:
   - pfSense blocking
   - Active Directory actions (when applicable)
   - Velociraptor quarantine/response (when applicable)

## Severity mapping
Based on Wazuh `rule.level`:
- **Low:** 0–7
- **Medium:** 8–12
- **High:** 13–16

## Deduplication
Workflows implement a guard/counter to avoid duplicate actions for the same recurring event, keyed by:
- `rule.id + srcip + agent.name`

## Diagrams (add your own)
- Architecture: `docs/diagrams/architecture.png`
- Network zones: `docs/diagrams/network-zones.png`
- Workflow sequence: `docs/diagrams/workflow-sequence.png`
