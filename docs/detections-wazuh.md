# Wazuh Detections (Rules)

Wazuh rules used in CyberSentinels are stored in `wazuh/rules/`.

## Included rule files
- `local_rules.xml`
- `ssh.xml` (SSH auth failures / brute force)
- `sudo.xml` + `priv.xml` (sudo execution / privilege-related detections)
- `login_failed.xml` (Windows + syslog login failures)
- `powershell_commands.xml` (suspicious PowerShell usage)
- `cipher_rules.xml` (cipher.exe execution)
- `files.xml`, `file_modif.xml`, `files_deleted.xml` (file integrity add/modify/delete)

## Notes for reviewers
- The XML files are included as used in the project.
- If you publish this repository publicly, consider whether internal hostnames/IPs should be sanitized.
