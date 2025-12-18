# Incident Response Playbooks

This section documents how the SOC is expected to handle key incident categories.

## SSH Brute Force
- Detection: repeated SSH auth failures
- Automation: Alert→Case, notify, optional pfSense block (high severity / IOC match)
- Analyst: validate scope, confirm/rollback block

## Privilege Escalation (Linux sudo)
- Detection: sudo executed / privilege patterns
- Automation: Case + enrichment + notify, optional response
- Analyst: validate command context and investigate follow-on activity

## Suspicious PowerShell
- Detection: encoded commands / risky cmdlets
- Automation: Case + enrichment + notify, optional Velociraptor/AD response based on context
- Analyst: validate endpoint chain and confirm/rollback actions

## File Integrity Change
- Detection: file add/modify/delete
- Automation: Alert→Case + notify, optional containment decision
- Analyst: validate change management vs compromise
