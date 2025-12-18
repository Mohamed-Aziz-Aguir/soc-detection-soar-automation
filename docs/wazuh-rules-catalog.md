# Wazuh Rules Catalog

The rule XML files used by SOC Operations Center are included in `wazuh/rules/`.

| Rule ID | Level | Description | MITRE | Source file |
|---:|---:|---|---|---|
| 100001 | 5 | sshd: authentication failed from IP 1.1.1.1. |  | local_rules.xml |
| 100010 | 7 | Possible cipher.exe excution detected |  | cipher_rules.xml |
| 100045 | 7 | Linux: Sudo command executed on $(agent.name) - Command: $(audit.command) |  | priv.xml |
| 100046 | 12 | Linux: Sudo executed sensitive command on $(agent.name) - Command: $(audit.command) |  | priv.xml |
| 100047 | 12 | Linux: Successful change to /etc/sudoers on $(agent.name) by user $(audit.uid) via $(audit.exe) |  | priv.xml |
| 100048 | 10 | Linux: Setuid binary executed on $(agent.name) - Command: $(audit.command) |  | priv.xml |
| 100049 | 11 | Linux: User group modified on $(agent.name) - Command: $(audit.command) |  | priv.xml |
| 100050 | 12 | Linux: Sensitive file permissions changed on $(agent.name) - File: $(audit.file) |  | priv.xml |
| 100051 | 8 | Linux: Failed privilege escalation attempt on $(agent.name) - Command: $(audit.command) |  | priv.xml |
| 100201 | 8 | Encoded command executed via PowerShell. | T1059.001, T1562.001 | powershell_commands.xml |
| 100202 | 4 | Windows Security blocked malicious command executed via PowerShell. | T1059.001 | powershell_commands.xml |
| 100203 | 10 | Risky CMDLet executed. Possible malicious activity detected. | T1059.001 | powershell_commands.xml |
| 100204 | 8 | Mshta used to download a file. Possible malicious activity detected. | T1059.001 | powershell_commands.xml |
| 100205 | 5 | PowerShell execution policy set to bypass. | T1059.001 | powershell_commands.xml |
| 100206 | 5 | Invoke Webrequest executed, possible download cradle detected. | T1059.001 | powershell_commands.xml |
| 100535 | 5 | Powershell Information EventLog |  | local_rules.xml |
| 100536 | 4 | Powershell executed : $(win.eventdata.ScriptBlockText) | T1083 | local_rules.xml |
| 100537 | 10 | Powershell Error EventLog |  | local_rules.xml |
| 100538 | 13 | Powershell Critical EventLog |  | local_rules.xml |
| 100540 | 5 | Logon Failure - Unknown user or bad passwords | T1531 | login_failed.xml |
| 100541 | 5 | syslog: User authentication failure. |  | login_failed.xml |
| 100550 | 7 | File added to sensetive location. |  | files.xml |
| 100558 | 8 | File modified in a sensetive location. |  | file_modif.xml |
| 100559 | 9 | File deleted from sensetive location. |  | files_deleted.xml |
| 100567 | 10 | Successful sudo executed. | T1548.003 | sudo.xml |
| 104521 | 10 | sshd: authentication failed. | T1021.004, T1110.001 | ssh.xml |
