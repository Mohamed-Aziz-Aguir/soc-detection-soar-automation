# Detection Engineering (Wazuh)

## Overview
Custom correlation rules were created to improve detection fidelity and enable automated incident handling.

For each detection, document:
- Intent (what behavior it detects)
- Required telemetry/fields
- MITRE ATT&CK mapping (where applicable)
- False positives and tuning notes
- SOAR actions triggered (case creation, enrichment, notifications, response)

## Example detections covered
- SSH brute force / repeated login failures
- Privilege escalation indicators (e.g., sudo usage patterns)
- Authentication anomalies
- File integrity events (if enabled)

## Rule catalog (fill in)
| Rule ID | Name | Level | Group | MITRE | Triggered workflow |
|---:|---|---:|---|---|---|
| {{RULE_ID}} | {{RULE_NAME}} | {{LEVEL}} | {{GROUP}} | {{Txxxx}} | {{WORKFLOW}} |

## Per-rule template (copy/paste)
### Rule {{RULE_ID}} — {{RULE_NAME}}
- **Goal:** {{What it detects}}
- **Telemetry:** {{Log source(s) and required fields}}
- **Logic (summary):** {{Conditions / thresholds}}
- **MITRE:** {{Technique / Sub-technique}}
- **False positives:** {{Expected benign scenarios}}
- **Tuning notes:** {{Exclusions / thresholds}}
- **SOAR actions:** {{Case creation, enrichment, notifications, response}}
- **Validation:** {{How you tested}}
