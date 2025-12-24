# SOC Operations Center — Detection & SOAR Automation  
**By CyberSentinels**

This repository documents an academic **SOC Operations Center** project that simulates a realistic internal Security Operations Center (SOC) with automated detection, incident response, enrichment, and case management.

The project demonstrates how security events are detected, correlated, enriched, escalated, and responded to using an integrated **SIEM + SOAR + Case Management** architecture.

---

## Project Overview

The SOC Operations Center is designed to model real-world SOC operations, including:

- Security event detection and correlation  
- Automated response and containment  
- Incident and case management  
- Threat intelligence enrichment  
- SOC operational metrics and visibility  
- Audit-oriented reporting and compliance alignment  

This repository is **documentation-focused** and presents the architecture, workflows, and operational logic used throughout the project.

---

## High-Level Architecture

Core components used in the SOC:

- **Wazuh** — SIEM and detection engine  
- **Shuffle** — SOAR orchestration and automation  
- **TheHive** — Incident and case management  
- **Cortex** — Automated enrichment and analysis  
- **MISP** — Threat intelligence correlation  
- **pfSense** — Network-level response and blocking  
- **Active Directory** — Identity-based containment  
- **Velociraptor** — Endpoint isolation and response  
- **Discord / Slack** — SOC notifications  

Architecture documentation and rendered diagrams are available here:  
➡️ `architecture/architecture.md`  

An interactive HTML version of the architecture is available via GitHub Pages:  
➡️ `docs/index.html`

---

## Repository Structure

```
soc-detection-soar-automation/
├── demo/
├── architecture/
├── soc-process/
├── shuffle/
├── wazuh/
├── mitre/
├── automation/
├── ai-audit/
├── compliance/
```

Each directory represents a specific SOC domain and is documented independently.

---

## Demo & Evidence

The `demo/` directory contains visual and video evidence of the SOC in operation, including dashboards, alerts, workflows, and case handling.

➡️ `demo/`

---

## Architecture Documentation

The `architecture/` directory documents:

- SOC architecture and integrations  
- Network segmentation and zoning  
- Data flows between security tools  
- Diagram slots and rendered diagrams  

➡️ `architecture/`  
➡️ `architecture/diagrams/`

---

## SOC Process & Operations

The `soc-process/` directory defines how the SOC operates from an analyst perspective, including:

- Incident lifecycle (alert → case → closure)  
- Severity classification model  
- Response and automation policy  
- Escalation model (Tier 1 / Tier 2 / IR Lead)  
- Metrics and KPIs (MTTD, MTTR, automation rate)  
- Analyst playbooks (SOPs)  

➡️ `soc-process/`  
➡️ `soc-process/playbooks/`

---

## Detection Engineering (Wazuh)

The `wazuh/` directory contains all detection logic used in the SOC:

- Custom and modified Wazuh rules (XML)  
- Rules validated in the lab environment  
- Each rule mapped to a dedicated SOAR workflow  

➡️ `wazuh/`  
➡️ `wazuh/rules/`

---

## SOAR Workflows (Shuffle)

The `shuffle/` directory documents all SOAR workflows used for automation:

- One workflow per detection scenario  
- Explicit execution order and actions  
- Case creation, enrichment, response, and notification logic  
- Sanitized workflow exports for reference  

➡️ `shuffle/`  
➡️ `shuffle/workflows/`  
➡️ `shuffle/exports/`

---

## MITRE ATT&CK Mapping

The `mitre/` directory maps detections and workflows to the **MITRE ATT&CK** framework:

- Technique-level ATT&CK mapping  
- ATT&CK Navigator layer for visual coverage  

➡️ `mitre/`

---

## Automation Scripts

The `automation/` directory contains supporting automation logic:

- Python scripts used by SOAR workflows  
- API-driven response actions  
- Routing, parsing, and deduplication logic  

➡️ `automation/`

---

## AI Audit Automation

The `ai-audit/` directory documents an AI-assisted audit automation pipeline developed as part of the same academic project:

- Automated audit report generation  
- NLP, OCR, and anomaly detection techniques  
- Analyst-focused summaries and compliance-oriented outputs  

➡️ `ai-audit/`

---

## Compliance & Standards Alignment

The `compliance/` directory provides high-level alignment with common security standards:

- NIST SP 800-61 (Incident Handling)  
- ISO/IEC 27001 (Operational Security)  
- PCI-DSS, SWIFT, Basel (reporting-oriented references)  

➡️ `compliance/`

---

## Project Context

- **Type**: Academic SOC simulation project  
- **Focus**: Detection engineering, SOAR automation, incident response operations  
- **Goal**: Demonstrate realistic SOC workflows and engineering practices  
- **Creators**: CyberSentinels  

This repository is intended for educational, portfolio, and demonstration purposes.
