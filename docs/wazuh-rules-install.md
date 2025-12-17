# Installing the Wazuh Rules (Minimal change)

This repo ships your rules as separate XML files in:
- `rules/wazuh/source/`

## Recommended minimal approach
1. Copy the XML content you want into your Wazuh `local_rules.xml` (or include as separate file if your deployment supports it).
2. Restart Wazuh manager.
3. Validate:
   - rule load success
   - alerts fire as expected
   - webhook routing to Shuffle for the intended rule IDs

## Rule files included
- `cipher_rules.xml` — cipher.exe execution detection
- `powershell_commands.xml` — suspicious PowerShell activity
- `login_failed.xml` — Windows + syslog authentication failures
- `ssh.xml` — SSH auth failures / brute force
- `sudo.xml` and `priv.xml` — Linux sudo / privilege change detections
- `files.xml`, `file_modif.xml`, `files_deleted.xml` — file integrity add/modify/delete

## Notes (keep as-is)
Some rules include compliance group tags (PCI-DSS, NIST, GDPR, etc.) and MITRE IDs. These are preserved.
