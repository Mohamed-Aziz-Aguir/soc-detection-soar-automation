# MITRE ATT&CK Mapping — SOC Operations Center

This document maps implemented **Wazuh detections** and **Shuffle SOAR workflows** to the **MITRE ATT&CK** framework.  
It is intentionally limited to what was built and demonstrated in this project.

## Legend
- **Detection Source**: Wazuh rule / log source
- **Workflow**: Shuffle SOAR workflow name
- **Automation**: Auto / Semi‑Auto / Manual (from the project design)

---

## Authentication & Access Attacks

| Detection / Use Case | MITRE Tactic | MITRE Technique | Workflow | Automation |
|---|---|---|---|---|
| SSH login failed (brute-force attempts) | Credential Access | **T1110 — Brute Force** | `ssh-login-failed` | Auto |
| AD login attempts failed (threshold lockout) | Credential Access | **T1110.001 — Password Guessing** | `login-attempt` | Auto |
| Repeated auth failures suggesting attempted misuse | Defense Evasion / Persistence | **T1078 — Valid Accounts** (attempted / precursor signals) | `login-attempt` | Semi‑Auto* |

\*Semi‑Auto because validation and tuning are analyst-driven; enforcement may be automated in your lab.

---

## Privilege Escalation

| Detection / Use Case | MITRE Tactic | MITRE Technique | Workflow | Automation |
|---|---|---|---|---|
| Windows privilege escalation detection | Privilege Escalation | **T1068 — Exploitation for Privilege Escalation** | `windows-privilege-escalation` | Auto |
| Linux privilege escalation detection | Privilege Escalation | **T1068 — Exploitation for Privilege Escalation** | `linux-privilege-escalation` | Auto |
| `sudo` executed / suspicious sudo activity | Privilege Escalation | **T1548.003 — Abuse Elevation Control Mechanism: Sudo and Sudo Caching** | `sudo-executed` | Auto |

---

## Execution, Malware, and Impact

| Detection / Use Case | MITRE Tactic | MITRE Technique | Workflow | Automation |
|---|---|---|---|---|
| Encoded PowerShell command execution | Execution | **T1059.001 — Command and Scripting Interpreter: PowerShell** | `powershell-encoded` | Auto |
| `cipher.exe` execution (ransomware-like indicator) | Impact | **T1486 — Data Encrypted for Impact** | `cipher-exe` | Auto |

---

## File Integrity, Defense Evasion, and Persistence

| Detection / Use Case | MITRE Tactic | MITRE Technique | Workflow | Automation |
|---|---|---|---|---|
| File modified (potential persistence/config tampering) | Persistence | **T1547 — Boot or Logon Autostart Execution** (possible; path-dependent) | `file-integrity` | Semi‑Auto |
| File deleted (indicator removal) | Defense Evasion | **T1070 — Indicator Removal on Host** | `file-integrity` | Semi‑Auto |
| File creation in sensitive paths (staging/persistence) | Defense Evasion / Persistence | **T1547** (possible; path-dependent) | `file-integrity` | Semi‑Auto |

---

## Notes
- Enrichment via **Cortex analyzers** (e.g., VirusTotal/Shodan/DomainTools) is used to increase confidence before or after response.
- Threat intel correlation (MISP) can elevate severity and change automation thresholds.
- This mapping is portfolio-focused and may include “possible/path-dependent” techniques where file paths or context determines the final ATT&CK technique.
