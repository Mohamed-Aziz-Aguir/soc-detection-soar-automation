# Lessons Learned

## What worked well
- Webhook-driven SOAR reduced manual effort for case creation and notifications.
- Standardized case formatting improved investigation consistency.
- Enrichment via Cortex/MISP provided faster context for analyst decisions.
- Firewall auto-block workflow reduced response time for clearly malicious sources.

## What caused noise / false positives (fill in)
- {{Example: internal scanners / admin activity / scheduled jobs}}
- {{Example: repeated benign login failures from known sources}}

## Improvements planned (fill in)
- Add cross-alert deduplication and time windows to prevent case flooding.
- Strengthen webhook authentication and rate limiting.
- Add a test harness with sample payloads to validate workflow changes.
- Add metrics (alert→case latency, volume by rule, false-positive rate).
