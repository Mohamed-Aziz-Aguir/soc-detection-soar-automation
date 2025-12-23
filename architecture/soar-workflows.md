# SOAR Workflows (Shuffle)

Platform-wide behavior:
- Create TheHive Alert, then promote to Case (Alert → Case) when conditions match
- Enrichment occurs after case creation (Cortex analyzers)
- Notifications sent to Discord + Slack
- Conditional response paths: pfSense / Active Directory / Velociraptor

Dedupe (partial):
- Not all workflows implement dedupe.
- Where implemented: rule.id + srcip + agent.name

Workflow catalog (curated):
| File | Category | Typical actions |
|---|---|---|
| file_integrity.json | file add/modify/delete | Alert→Case + Discord notify |
| sudo_executed.json | sudo activity | Case + Velociraptor quarantine + Active Directory action (both) |
| cipher_execution.json | cipher.exe | Case + pfSense block + Velociraptor lockdown |
| login_attempt.json | login failures | AD block after 3 failures/3 minutes |
| ssh_login_failed.json | SSH brute force | Alert→Case + Cortex enrichment + pfSense block |
| windows_privilege_activity.json | Windows priv activity | Case + containment path depending on trigger |

Enrichment analyzers used:
- VirusTotal
- Shodan
- DomainTools
