from langgraph.graph import StateGraph, START, END

from graph.state import SOCState

from agents.log_collector import log_collector
from agents.threat_detector import threat_detector
from agents.investigator import investigator
from agents.threat_intel import threat_intel
from agents.risk_assessor import risk_assessor
from agents.response_agent import response_agent
from agents.report_generator import report_generator

workflow = StateGraph(SOCState)

workflow.add_node(
    "report_generator",
    report_generator
)
workflow.add_node(
    "response_agent",
    response_agent
)
workflow.add_node(
    "risk_assessor",
    risk_assessor
)
workflow.add_node(
    "threat_intel",
    threat_intel
)
workflow.add_node("log_collector", log_collector)
workflow.add_node("threat_detector", threat_detector)
workflow.add_node("investigator", investigator)


workflow.add_edge(START, "log_collector")
workflow.add_edge("log_collector", "threat_detector")

def threat_router(state: SOCState):
    if state["is_threat"]:
        return "investigator"

    return END


workflow.add_conditional_edges(
    "threat_detector",
    threat_router
)

workflow.add_edge(
    "investigator",
    "threat_intel"
)

workflow.add_edge(
    "threat_intel",
    "risk_assessor"
)

workflow.add_edge(
    "risk_assessor",
    "response_agent"
)

workflow.add_edge(
    "response_agent",
    END
)

workflow.add_edge(
    "response_agent",
    "report_generator"
)

workflow.add_edge(
    "report_generator",
    END
)
graph = workflow.compile()