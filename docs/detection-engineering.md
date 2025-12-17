# Detection Engineering

For each detection (rule) document:
- **Intent**: what attacker/behavior it detects
- **Telemetry**: required log sources / fields
- **Logic**: matching conditions
- **MITRE ATT&CK**: technique mapping
- **False positives**: expected benign matches + tuning notes
- **Response**: suggested analyst actions / playbook

## Rule catalog
Add a table of your custom rules:
| Rule ID | Name | Severity | MITRE | Primary fields |
|---|---|---:|---|---|

## Validation
Describe how you validated detections (test logs, atomic tests, replay of sample events, etc.).
