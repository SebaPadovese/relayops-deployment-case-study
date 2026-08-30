# Implementation Risk Register

| Risk | Impact | Treatment | Release decision |
|---|---|---|---|
| False negative on life safety | Critical | Mandatory risk question, broader triggers, full P1 regression suite | Block release |
| Permission failure | Critical | Verify least-privilege roles and audit events | Remove launch access |
| False positive escalation | Medium | Tune only after safety coverage remains intact | Monitor during pilot |
| Incomplete submission | Medium | Improve required fields, examples and training | Fix before automation |
| Unsupported policy answered as fact | High | Route to client authority and forbid invented answers | Block affected workflow |
| Low frontline adoption | Medium | Scenario training, site champions and daily pilot feedback | Extend pilot |

