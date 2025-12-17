# Detection Engineering (Wazuh) — CyberSentinels

## Rule sources
Your custom rules are stored in `rules/wazuh/source/` as provided.

## Catalog
See `docs/wazuh-rules-catalog.md` for a summarized table of rule IDs, levels, descriptions, and MITRE mappings (where present).

## How to load (documentation-only)
Typical Wazuh locations:
- `local_rules.xml` for local custom rules
- Additional XML files can be merged into local rules or included depending on your deployment approach.

> This repository does not enforce a single deployment method; it documents the existing rules and their intended purpose.

## Mapping detections to SOAR
For each rule you automate, add:
- the rule ID
- expected alert fields
- workflow name (Shuffle)
- response policy (notify-only vs case + block)
