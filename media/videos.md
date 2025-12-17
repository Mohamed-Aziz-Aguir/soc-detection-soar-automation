# Demo Video — CyberSentinels

- YouTube: https://www.youtube.com/watch?v=DYTV5zdeY8U

## Intended narrative (what the demo should communicate)
This demo should clearly answer:
1. **Who we are:** CyberSentinels (student SOC initiative)
2. **What we built:** an integrated SOC platform (SIEM + SOAR + case management + enrichment + TI)
3. **How it works:** end-to-end incident handling pipeline (Wazuh → Shuffle → TheHive → Cortex → Discord/Slack; with optional auto-block)
4. **What is verified:** screenshots/workflows/rules exported in this repo

## Suggested talk track (template)
### 0) Intro (Who we are)
- CyberSentinels is a student-driven team building a simulated SOC.
- Goal: mirror real-world SOC processes: detection, triage, response, enrichment, and documentation.

### 1) Architecture overview
- Show the architecture diagram (slot in repo: `docs/diagrams/architecture.png`).
- Explain tool roles:
  - Wazuh = SIEM/detections
  - Shuffle = SOAR/orchestration
  - TheHive = case management
  - Cortex = analyzers/enrichment
  - MISP = threat intel IOC correlation
  - Discord/Slack = SOC notifications
  - Firewall block workflow = automated response

### 2) Application walkthrough (UI)
- Show SOC Operations dashboard mock-up (screenshots in `media/screenshots/`).
- Explain key widgets: active cases, alerts, workflows, avg response time, tool health.

### 3) Incident flow demo
- Trigger one scenario (e.g., SSH brute force / PowerShell encoded command / sudo sensitive command).
- Show:
  - Wazuh alert → Shuffle webhook intake
  - Shuffle decisions (severity + dedupe)
  - TheHive case creation/update
  - Cortex analyzers triggered (VirusTotal/Shodan/DomainTools)
  - Notification to Discord/Slack
  - Auto-block workflow (if used in this scenario)

### 4) Closing
- Summarize impact: reduced manual triage steps, faster response, consistent case structure.
- Mention documentation and audit-readiness.

## Timestamp slots (fill in)
- 00:00 — Intro (who we are)
- 00:XX — Architecture overview
- 00:XX — Dashboard mock-up walkthrough
- 00:XX — Live incident scenario
- 00:XX — Response + enrichment + notifications
- 00:XX — Conclusion
