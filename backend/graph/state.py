from typing import TypedDict


class SOCState(TypedDict):
    # Input
    raw_logs: list[dict]
    parsed_logs: list[dict]

    # Detection
    is_threat: bool
    threat_score: float

    # Investigation
    investigation_result: dict
    threat_intelligence: dict

    # Risk Assessment
    severity: str

    # Response
    recommended_action: list[str]
    is_human_approved: bool

    # Report
    incident_timeline: list[str]
    incident_report: str

    # Errors
    errors: list[str]