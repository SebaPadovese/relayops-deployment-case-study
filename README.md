# Sebastian Padovese — Operations Portfolio

**Operations · Program Delivery · Implementation · People & Process**

Gorizia, Italy · EU work authorisation  
Italian & Spanish (native) · English (C2) · Portuguese (B2)

I work where **people, processes, information and service delivery** meet.

My background spans cultural and public-facing operations, international service environments and independent implementation work. In practice, that has meant coordinating staffing, supporting colleagues, maintaining operational records, communicating with institutional and external stakeholders, improving recurring workflows, and turning ambiguous operational problems into clearer systems.

This repository brings together **real-world anonymised case studies** and **RelayOps**, an independent implementation simulation. The aim is simple: show how I approach operations rather than ask an employer to infer it from job titles.

## Start here — 90-second evidence map

| If you want to see… | Read |
|---|---|
| How I coordinate real-world service operations and stakeholders | **[Field Operations — Multi-Site Cultural Services](case-studies/field-operations-cultural-services.md)** |
| How I approach staffing, employee support, recruitment input and escalation | **[Workforce Operations — Support, Staffing & Retention](case-studies/workforce-operations.md)** |
| How I approach fragmented spreadsheets, reporting and workflow improvement | **[Operational Data & Reporting — From Fragmented Files to Usable Information](case-studies/operational-data-reporting.md)** |
| How I design an implementation from requirements through testing and rollout | **[RelayOps — Implementation Simulation](#relayops-implementation-simulation)** |

## Real-world operations case studies

### 1. Field Operations — Multi-Site Cultural Services

An anonymised case based on my work in cultural and public-facing services in Italy.

It covers the operating layer between frontline delivery, workforce coordination, public institutions, suppliers, organised groups and reporting — including how I approach ownership, communication and recurring procedures without adding unnecessary bureaucracy.

**[Read the case study →](case-studies/field-operations-cultural-services.md)**

### 2. Workforce Operations — Support, Staffing & Retention

A case focused on the people side of small-team operations: staffing coverage, practical employee support, issue triage, escalation, recruitment input and retention context.

It deliberately distinguishes operational responsibility from formal HR authority. The goal is reliable support and better information flow, not inflated titles.

**[Read the case study →](case-studies/workforce-operations.md)**

### 3. Operational Data & Reporting — From Fragmented Files to Usable Information

A case about improving recurring spreadsheet and reporting workflows while preserving historical data.

The approach is **source data → validation → aggregation → reporting**, with AI used as an analysis and documentation assistant while source records and human review remain authoritative.

**[Read the case study →](case-studies/operational-data-reporting.md)**

---

## RelayOps — Implementation Simulation

[![Verification](https://github.com/SebaPadovese/relayops-deployment-case-study/actions/workflows/verify.yml/badge.svg)](https://github.com/SebaPadovese/relayops-deployment-case-study/actions/workflows/verify.yml)

RelayOps is an independent implementation simulation for an AI-assisted, multi-site public-service workflow. It demonstrates the delivery discipline behind an implementation: discovery, requirements, routing, governance, UAT, training, staged rollout, go-live criteria and measurement.

**[Read the complete six-page RelayOps case study (PDF)](portfolio/RelayOps_Deployment_Case_Study_Sebastian_Padovese.pdf)**

The scenario is fictional. The operating judgment is grounded in my real experience across public-facing cultural sites. RelayOps does **not** represent a client engagement, production deployment, API integration, live user base, validated NLP model or achieved ROI.

### What is executable

The prototype applies deterministic P1–P4 routing rules to structured incident records. Twelve multilingual UAT cases cover Italian, Spanish, English and Brazilian Portuguese. Tests verify priority, owner, response target and safety guardrails.

```bash
python -m unittest discover -s tests -v
PYTHONPATH=src python -m relayops.cli data/uat_cases.json
```

No third-party dependencies are required. GitHub Actions repeats compilation, acceptance-test and multilingual UAT checks on Python 3.10, 3.12 and 3.13.

### RelayOps evidence map

| Employer question | Evidence |
|---|---|
| Can you translate operations into requirements? | [Requirements matrix](docs/requirements_matrix.md) |
| Can you design ownership and escalation? | [Routing logic](src/relayops/routing.py) · [Governance](docs/governance.md) |
| Can you test before launch? | [UAT cases](data/uat_cases.json) · [Tests](tests/test_routing.py) · [Execution report](docs/uat_execution_report.md) |
| Can you plan delivery and adoption? | [Rollout plan](docs/rollout_plan.md) |
| Can you manage implementation risk? | [Risk register](docs/risk_register.md) |
| Are the claims defensible? | [Truth boundary](docs/truth_boundary.md) |

### Design principle

AI may reduce intake friction by summarising, translating or suggesting a category. Safety, authority, ownership and closure remain deterministic and human-controlled. A P1 incident always forces human takeover; unsupported policy requests are sent for confirmation rather than answered as fact.

---

## What connects the work

Across the real cases and the simulation, the same operating principles recur:

1. **Understand the actual workflow before redesigning it.**
2. **Make ownership and escalation explicit.**
3. **Preserve reliable source information.**
4. **Automate repetition, not judgment.**
5. **Design for the person who has to use the process next.**
6. **Document enough that the system does not depend on one person's memory.**

## Roles I am targeting

I am interested in international roles across **Operations, Program Operations, Project Operations, Implementation, Deployment and adjacent People/Learning Operations**, particularly where the work involves coordinating stakeholders, improving processes, supporting teams and making complex operations easier to run.

## Contact

**Sebastian Padovese**  
Gorizia, Italy · EU work authorisation  
[LinkedIn](https://www.linkedin.com/in/sebastian-padovese-bb61372b7)

---

### Repository structure

```text
case-studies/          Anonymised real-world operations cases
data/                  Structured multilingual RelayOps UAT cases
docs/                  RelayOps requirements, governance, rollout and risks
portfolio/             Presentation-ready RelayOps case study
src/relayops/          Executable routing prototype and CLI
tests/                 Automated acceptance tests
```

### Truth boundary

The three field case studies are anonymised descriptions of real operational work. RelayOps is an independent simulation. Neither should be represented as paid consulting or as a production software deployment unless explicitly stated otherwise in the relevant case.

### License

Source code in `src/` and automated tests in `tests/` are available under the MIT License in [`LICENSE-CODE`](LICENSE-CODE). Documentation, repository narrative, portfolio PDF and UAT data are available under CC BY-NC 4.0 in [`LICENSE-DOCUMENTATION.md`](LICENSE-DOCUMENTATION.md).
