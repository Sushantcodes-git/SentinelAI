from graph.state import SOCState
from prompts.investigation_prompt import INVESTIGATION_PROMPT
from services.llm_service import llm
from models.investigation import InvestigationResult


def investigator(state: SOCState) -> SOCState:

    logs = state["parsed_logs"]

    prompt = f"""
{INVESTIGATION_PROMPT}

Security Logs:

{logs}
"""

    structured_llm = llm.with_structured_output(InvestigationResult)

    result = structured_llm.invoke(prompt)

    state["investigation_result"] = result.model_dump()

    print("AI Investigation Completed")

    return state