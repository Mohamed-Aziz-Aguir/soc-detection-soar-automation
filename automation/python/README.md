# Custom Python Utilities

Custom Python was used to support:
- parsing/normalization of alert payloads
- deduplication helpers (where workflow-native methods were insufficient)
- routing decisions
- response actions (e.g., pfSense rule creation)

Included example:
- pfsense_block.py — adds a pfSense block rule for a given IP (credentials via environment variables)
