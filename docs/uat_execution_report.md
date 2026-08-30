# UAT Execution Report

**Scope:** deterministic priority, ownership, response-target and guardrail routing  
**Dataset:** `data/uat_cases.json`  
**Execution:** automated acceptance suite plus command-line runner  
**Result:** 12/12 structured scenarios passed; 2/2 negative-control tests passed

| ID | Language | Expected priority | Actual priority | Result |
|---|---|---:|---:|---|
| UAT-01 | IT | P1 | P1 | PASS |
| UAT-02 | ES | P1 | P1 | PASS |
| UAT-03 | EN | P2 | P2 | PASS |
| UAT-04 | PT-BR | P2 | P2 | PASS |
| UAT-05 | IT | P2 | P2 | PASS |
| UAT-06 | ES | P3 | P3 | PASS |
| UAT-07 | EN | P3 | P3 | PASS |
| UAT-08 | PT-BR | P3 | P3 | PASS |
| UAT-09 | IT | P4 | P4 | PASS |
| UAT-10 | ES | P4 | P4 | PASS |
| UAT-11 | EN | P4 | P4 | PASS |
| UAT-12 | PT-BR | P4 | P4 | PASS |

## Negative controls

- Incomplete records are rejected before routing.
- Unknown categories are rejected rather than silently assigned a default.

## Interpretation

This run verifies the written deterministic logic against the structured test dataset. It does not validate free-text classification, production integration, platform resilience, customer adoption or business impact.

