from graph.state import SOCState


def threat_detector(state: SOCState) -> SOCState:
    """
    Detects suspicious activities from logs.
    """

    failed_logins = 0

    for log in state["parsed_logs"]:

        if log["event"] == "Failed Login":
            failed_logins += 1

    if failed_logins > 0:
        state["is_threat"] = True
        state["threat_score"] = 75

    else:
        state["is_threat"] = False
        state["threat_score"] = 0

    print("Threat Detection Agent Executed")

    return state