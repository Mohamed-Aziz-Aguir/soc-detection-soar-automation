# SOC Operations Center — Detection & SOAR Automation  
**By CyberSentinels**

Award-winning academic project presented at **Bal de Projet ESPRIT**, implementing a full-scale Security Operations Center (SOC) with detection engineering, SOAR automation, and incident response.

---

## Overview

This project simulates a realistic SOC environment integrating:

- Security event detection and correlation  
- Automated incident response (SOAR)  
- Threat intelligence enrichment  
- Case management and investigation workflows  
- SOC metrics and operational visibility  

The system processes alerts end-to-end — from detection to response — across multiple attack scenarios.

---

## SOC Pipeline

```
Endpoints (Windows / Linux)
        ↓
Wazuh Agents
        ↓
Wazuh Manager (SIEM)
        ↓ (Webhook)
Shuffle (SOAR)
        ↓
- Enrichment (Cortex / MISP)
- Case Management (TheHive)
- Response (pfSense / AD / Velociraptor)
        ↓
Notifications (Discord / Slack)
```

---

## Key Capabilities

- Detection engineering with custom Wazuh rules  
- Automated response via Shuffle workflows  
- Threat intelligence correlation (MISP, Cortex)  
- Incident lifecycle management (TheHive)  
- MITRE ATT&CK mapping  
- SOC metrics (MTTD, MTTR, automation rate)  

---

## Detection Scenarios

### Windows
- Privilege Escalation  
- Suspicious Login Activity  
- Cipher Abuse  

### Linux
- Privilege Escalation  
- SSH Brute Force  

### Monitoring
- File Integrity Violations  

Each scenario is:
- Detected by Wazuh agents  
- Forwarded via webhook  
- Processed by a dedicated SOAR workflow  
- Enriched, escalated, and responded automatically  

---

## Example Workflow

### Windows Privilege Escalation

**Detection**
- Source: Wazuh Agent  
- Trigger: Suspicious privilege assignment  

**Flow**
1. Alert generated in Wazuh  
2. Webhook sent to Shuffle  
3. Workflow execution:
   - Parse and validate alert  
   - Enrich indicators (Cortex / MISP)  
   - Create case in TheHive  
   - Trigger response actions  
   - Send SOC notification  

**Outcome**
- Automated case creation  
- Enriched alert context  
- Immediate SOC visibility and response  

---

## Architecture

Detailed documentation and diagrams:

- `architecture/architecture.md`  
- `architecture/diagrams/`  
- `docs/index.html` (interactive view)

---

## Repository Structure

```
soc-detection-soar-automation/
├── demo/            # Dashboards, alerts, workflows (evidence)
├── architecture/    # SOC design & diagrams
├── soc-process/     # Incident lifecycle & playbooks
├── wazuh/           # Detection rules
├── shuffle/         # SOAR workflows
├── mitre/           # ATT&CK mapping
├── automation/      # Scripts & integrations
├── ai-audit/        # AI-assisted audit pipeline
├── compliance/      # Standards alignment
```

---

## Results

- Multi-environment attack detection (Windows & Linux)  
- Automated incident handling via SOAR workflows  
- Reduced manual investigation effort through enrichment  
- Scalable SOC architecture design  

---

## Project Context

- Type: Academic SOC simulation  
- Event: Bal de Projet ESPRIT (award-winning project)  
- Team: CyberSentinels  
- Focus: Detection Engineering, SOAR Automation, Incident Response  
