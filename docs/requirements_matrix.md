# Requirements Matrix

| ID | User / stakeholder | Requirement | Acceptance evidence |
|---|---|---|---|
| FR-01 | Frontline staff | Submit site, language, category, description and immediate-risk status | Missing required fields are rejected |
| FR-02 | Site supervisor | Every accepted case receives one priority, owner, target and guardrail | Twelve UAT cases return complete decisions |
| FR-03 | Operations lead | View a shared P1-P4 taxonomy across sites | Routing catalogue is centralized in code |
| FR-04 | Client authority | Unsupported policy requests require confirmation | UAT-08 routes to client authority/operations |
| FR-05 | Visitors | Accessibility blockages receive urgent human ownership | UAT-03 returns P2 and facilities ownership |
| NFR-01 | Safety | Life-safety cases bypass ordinary queues | P1 forces immediate human takeover |
| NFR-02 | Privacy | Intake minimizes personal data | Prototype uses operational fields only |
| NFR-03 | Auditability | Decisions are reproducible from structured input | Deterministic rules and versioned test data |
| NFR-04 | Language | Operational examples cover IT, ES, EN and PT-BR | UAT dataset contains all four languages |

These are simulation requirements, not requirements approved by a real customer.

