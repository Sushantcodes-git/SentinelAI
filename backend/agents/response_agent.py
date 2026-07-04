from graph.state import SOCState


def response_agent(state: SOCState) -> SOCState:

    severity = state["severity"]

    if severity == "Critical":
        action = [
            "Block Source IP",
            "Disable User Account",
            "Isolate Endpoint",
            "Notify SOC Team Immediately"
        ]

    elif severity == "High":
        action = [
            "Block Source IP",
            "Force Password Reset",
            "Notify Security Team"
        ]

    elif severity == "Medium":
        action = [
            "Monitor Activity",
            "Force Password Reset"
        ]

    else:
        action = [
            "Continue Monitoring"
        ]

    state["recommended_action"] = action

    print("Response Agent Completed")

    return state