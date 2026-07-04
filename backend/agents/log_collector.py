from graph.state import SOCState


def log_collector(state: SOCState):

    print("Log Collector Agent Executed")

    state["parsed_logs"] = state["raw_logs"]

    return state