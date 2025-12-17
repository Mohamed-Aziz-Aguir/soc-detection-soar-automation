# CyberSentinels — SOC Platform Documentation

This repository contains **documentation and reference artifacts** for the CyberSentinels SOC platform: detections, automation workflows, and incident-handling processes.

CyberSentinels was designed as a realistic SOC environment integrating:
- **Wazuh** (SIEM / correlation)
- **Shuffle** (SOAR / orchestration)
- **TheHive** (case management: Alert → Case)
- **Cortex** (enrichment: VirusTotal, Shodan, DomainTools)
- **MISP** (threat intelligence IOC correlation)
- **pfSense** (network enforcement / blocking)
- **Active Directory** and **Velociraptor** (identity + endpoint response paths)
- **Discord + Slack** (SOC notifications)

> This is a **documentation-first** repository. It is intended for review, learning, and portfolio evidence.

## Evidence
- Screenshots: `assets/screenshots/`
- Demo video: `docs/demo-video.md` (YouTube link + talk track)

## Contents
- `docs/` — architecture, integrations, SOAR workflows, detections, IR playbooks
- `wazuh/rules/` — Wazuh rule XML files (as used in the project)
- `shuffle/workflows/` — Shuffle workflow exports (JSON)

## Diagram slots
Add your own exported diagrams here:
- `docs/diagrams/architecture.png`
- `docs/diagrams/network-zones.png`
- `docs/diagrams/workflow-sequence.png`
