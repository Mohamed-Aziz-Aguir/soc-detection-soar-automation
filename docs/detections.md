# Detections (Wazuh)

Wazuh rules are included in `wazuh/rules/` as used in the project.

## Rule catalog
See `docs/wazuh-rules-catalog.md` for rule IDs, levels, descriptions, and MITRE IDs where present.

## Engineering notes
- Rules are a mix of self-written detections and modified baseline rules.
- False positive reduction was attempted, but the tuning strategy is intentionally basic for an academic build.
- Every added detection was tested and wired to a corresponding Shuffle workflow.

## Recommended upgrades (future work)
- Consistent allowlists and tuning notes per rule
- A sample-payload replay pack for each rule/workflow
- Expand ATT&CK mapping coverage
