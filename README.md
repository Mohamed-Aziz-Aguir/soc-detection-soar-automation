# SOC Detection & SOAR Automation Portfolio

This repository documents an end-to-end SOC pipeline built around Wazuh detections and Shuffle SOAR workflows.

## What this project demonstrates
- Detection engineering: custom Wazuh rules for actionable security events
- SOAR automation: Wazuh webhook ingestion → enrichment/decisioning → ticket/case creation → notifications
- Incident handling: consistent case structure, severity mapping, and response actions
- Documentation-first delivery: architecture, integrations, and operational guidance

## Contents
- `docs/` — architecture, integrations, detection engineering notes, IR workflow, and lessons learned
- `rules/wazuh/` — Wazuh custom rules (redact secrets if any)
- `workflows/shuffle/` — Shuffle workflow exports (JSON)
- `media/` — screenshots and demo video links

## Quick start (documentation)
Start with:
1. `docs/architecture.md`
2. `docs/integrations.md`
3. `docs/detection-engineering.md`
4. `docs/soar-workflows.md`
5. `docs/incident-response.md`

## Demo
See `media/videos.md` for demo video links and timestamps.

## Notes
This repo documents a fully implemented SOC detection & SOAR automation project. Configuration files, workflow exports, and demonstrations are provided. Environment redeployment is outside the scope of this documentation.
