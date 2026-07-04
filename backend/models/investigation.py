from pydantic import BaseModel, Field


class InvestigationResult(BaseModel):
    attack_summary: str = Field(
        description="Short summary of the detected security incident."
    )

    attack_type: str = Field(
        description="Type of cyber attack detected."
    )

    severity: str = Field(
        description="Severity of the incident: Low, Medium, High, or Critical."
    )

    confidence: int = Field(
        ge=0,
        le=100,
        description="Confidence score between 0 and 100."
    )

    reasoning: str = Field(
        description="Detailed explanation of why the activity is considered suspicious."
    )

    mitre_attack: list[str] = Field(
        default_factory=list,
        description="Relevant MITRE ATT&CK techniques."
    )

    next_steps: list[str] = Field(
        default_factory=list,
        description="Recommended investigation and remediation steps."
    )