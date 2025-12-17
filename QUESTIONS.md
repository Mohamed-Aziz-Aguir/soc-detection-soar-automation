# Remaining questions (to make docs fully precise)

Answer briefly. If unknown, say "unknown" and we will document assumptions.

## 1) Dedupe key (important)
Your workflows use a counter/guard script. What is the dedupe key?
Examples:
- `rule.id + agent.name + srcip + 10m window`
- `rule.id + agent.id + user + 5m window`
Answer: {{...}}

## 2) Auto-block workflow scope
When do you block?
- Always on High severity?
- Only for brute force (SSH) with threshold?
- Only for IOC matches from MISP?
Answer: {{...}}

## 3) Rollback / unblock
How do you rollback an auto-block?
- Manual firewall rule removal?
- Automated unblock after N minutes?
Answer: {{...}}

## 4) Wazuh → Shuffle integration details (high level)
Which method do you use?
- Wazuh integration script + webhook URL?
- Custom script/active response?
Answer: {{...}}

## 5) TheHive case template
Do you use:
- Alert → Case conversion in TheHive
- Direct Case creation only
Answer: {{...}}
