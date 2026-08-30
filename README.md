# RelayOps Evidence Repository

RelayOps is an independent implementation simulation for an AI-assisted, multi-site public-service workflow. It demonstrates the delivery discipline behind an implementation: discovery, requirements, routing, governance, UAT, training, staged rollout, go-live criteria, and measurement.

The scenario is fictional. The operating judgment is grounded in Sebastian Padovese's real experience across public-facing cultural sites. This repository does **not** represent a client engagement, production deployment, API integration, live user base, validated NLP model, or achieved ROI.

## What is executable

The prototype applies deterministic P1-P4 routing rules to structured incident records. Twelve multilingual UAT cases cover Italian, Spanish, English, and Brazilian Portuguese. The tests verify priority, owner, response target, and safety guardrails.

```bash
python -m unittest discover -s tests -v
PYTHONPATH=src python -m relayops.cli data/uat_cases.json
```

No third-party dependencies are required.

## Evidence map

| Employer question | Evidence |
|---|---|
| Can you translate operations into requirements? | `docs/requirements_matrix.md` |
| Can you design ownership and escalation? | `src/relayops/routing.py` and `docs/governance.md` |
| Can you test before launch? | `data/uat_cases.json`, `tests/test_routing.py` and `docs/uat_execution_report.md` |
| Can you plan delivery and adoption? | `docs/rollout_plan.md` |
| Can you manage implementation risk? | `docs/risk_register.md` |
| Are the claims defensible? | `docs/truth_boundary.md` |

## Design principle

AI may reduce intake friction by summarizing, translating, or suggesting a category. Safety, authority, ownership, and closure remain deterministic and human-controlled. A P1 incident always forces human takeover; unsupported policy requests are sent for confirmation rather than answered as fact.

## Repository structure

```text
data/                 Structured multilingual UAT cases
docs/                 Requirements, governance, rollout, risks and boundaries
src/relayops/         Executable routing prototype and CLI
tests/                Automated acceptance tests
```

## License

Licensing is separated by artifact type:

- Source code in `src/` and automated tests in `tests/` are available under the MIT License in [`LICENSE-CODE`](LICENSE-CODE).
- Documentation, repository narrative, and UAT data are available under CC BY-NC 4.0 in [`LICENSE-DOCUMENTATION.md`](LICENSE-DOCUMENTATION.md).

## Portfolio use

Defensible description:

> Designed an end-to-end implementation simulation for an AI-assisted multi-site service workflow, covering discovery, requirements, P1-P4 routing, stakeholder governance, training, pilot rollout, go-live criteria, and KPI design. Built a deterministic routing prototype and executed twelve multilingual UAT scenarios.

Do not describe RelayOps as paid consulting, a production SaaS implementation, or a live customer deployment.
