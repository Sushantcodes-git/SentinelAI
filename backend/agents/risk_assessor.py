from graph.state import SOCState


def risk_assessor(state: SOCState) -> SOCState:

    investigation = state["investigation_result"]
    threat_intel = state["threat_intelligence"]

    severity = investigation["severity"]
    malicious_score = threat_intel["malicious_score"]

    # Risk Calculation
    if severity == "Critical":
        final_risk = "Critical"

    elif severity == "High":
        final_risk = "Critical" if malicious_score > 70 else "High"

    elif severity == "Medium":
        final_risk = "High" if malicious_score > 70 else "Medium"

    else:
        final_risk = "Medium" if malicious_score > 70 else "Low"

    state["severity"] = final_risk

    print("Risk Assessment Completed")

    return state