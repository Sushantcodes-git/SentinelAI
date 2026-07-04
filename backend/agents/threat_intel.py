from graph.state import SOCState
from tools.virus_total import check_ip


def threat_intel(state: SOCState) -> SOCState:

    ip = state["parsed_logs"][0]["ip"]

    intel = check_ip(ip)

    state["threat_intelligence"] = intel

    print("Threat Intelligence Completed")

    return state