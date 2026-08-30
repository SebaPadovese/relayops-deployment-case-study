from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class RoutingDecision:
    priority: str
    owner: str
    response_target: str
    guardrail: str
    human_takeover: bool = False


ROUTES: Mapping[str, RoutingDecision] = {
    "life_safety": RoutingDecision(
        "P1", "site_supervisor+emergency_services", "immediate",
        "no_automated_closure", True,
    ),
    "accessibility_block": RoutingDecision(
        "P2", "site_supervisor+facilities", "15_minutes",
        "supervisor_confirmation_required",
    ),
    "staffing_critical": RoutingDecision(
        "P2", "operations_lead", "15_minutes",
        "supervisor_confirmation_required",
    ),
    "security": RoutingDecision(
        "P2", "operations_lead", "15_minutes",
        "supervisor_confirmation_required",
    ),
    "facility_noncritical": RoutingDecision(
        "P3", "site_supervisor", "4_hours", "status_updates_required",
    ),
    "visitor_complaint": RoutingDecision(
        "P3", "site_supervisor", "4_hours", "status_updates_required",
    ),
    "unsupported_policy": RoutingDecision(
        "P3", "client_authority+operations_lead", "4_hours",
        "no_invented_answer_request_confirmation",
    ),
    "routine_information": RoutingDecision(
        "P4", "knowledge_workflow", "1_business_day", "human_available",
    ),
    "handover": RoutingDecision(
        "P4", "knowledge_workflow", "1_business_day", "human_available",
    ),
}


def route_case(case: Mapping[str, object]) -> RoutingDecision:
    """Route one structured case; reject incomplete or unknown categories."""
    required = ("id", "language", "category", "description")
    missing = [field for field in required if not case.get(field)]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    category = str(case["category"])
    try:
        return ROUTES[category]
    except KeyError as exc:
        raise ValueError(f"Unsupported category: {category}") from exc

