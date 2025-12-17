# Architecture

## High-level connections
- **Wazuh → (Alerts/Webhooks) → Shuffle**
- **Shuffle → (Case creation/updates) → TheHive**
- **TheHive → (Triggers analysis) → Cortex**
- **MISP → (IOC enrichment) → Wazuh & TheHive**
- **Shuffle → (Notifications) → Discord & Slack**
- **Shuffle → (Automated response) → Firewall (auto-block malicious IPs)**

## Reference diagram (Mermaid)
```mermaid
flowchart LR
    W[Wazuh\nSIEM & Correlation]
    S[Shuffle\nSOAR]
    H[TheHive\nCase Management]
    C[Cortex\nAutomated Analysis]
    M[MISP\nThreat Intelligence]
    V[Velociraptor\nEDR (optional)]
    N[Suricata\nNIDS (optional)]
    F[Firewall / pfSense (optional)]
    D[Discord]
    L[Slack]

    N -->|Network alerts| W
    V -->|Endpoint telemetry| W
    M -->|IOC feeds| W

    W -->|Alert webhook| S
    S -->|Create/Update Case| H
    H -->|Trigger analyzers| C
    C -->|Enrichment results| H
    M -->|IOC enrichment| H

    S -->|Notifications| D
    S -->|Notifications| L
    S -->|Auto-block IP (workflow)| F
```

## Environment context (lab)
A fully virtualized environment was deployed across multiple network zones (e.g., DMZ, LAN, SOC, IDS, Pentesting) with layered firewalls. The SOC stack integrates SIEM, SOAR, case management, enrichment, and threat intelligence for end-to-end incident handling.

## Design principles
- Automate repetitive SOC tasks (case creation, enrichment, notifications)
- Preserve analyst control for high-impact actions unless explicitly safe
- Standardize case structure, severity mapping, and observables
- Maintain audit-ready documentation and traceability
