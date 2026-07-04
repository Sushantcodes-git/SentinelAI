from fastapi import APIRouter

from graph.workflow import graph
from models.incident import LogRequest

router = APIRouter()


@router.post("/analyze")
def analyze_logs(request: LogRequest):

    initial_state = {
        "raw_logs": request.logs,
        "parsed_logs": [],
        "is_threat": False,
        "threat_score": 0,
        "investigation_result": {},
        "threat_intelligence": {},
        "severity": "",
        "recommended_action": [],
        "is_human_approved": False,
        "incident_timeline": [],
        "incident_report": "",
        "errors": []
    }

    result = graph.invoke(initial_state)

    return {
    "status": "success",

    "summary": {
        "severity": result["severity"],
        "threat_score": result["threat_score"],
        "attack_type": result["investigation_result"]["attack_type"],
        "confidence": result["investigation_result"]["confidence"]
    },

    "threat_intelligence": result["threat_intelligence"],

    "recommended_action": result["recommended_action"],

    "incident_report": result["incident_report"]
}