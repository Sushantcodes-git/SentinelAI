from services.llm_service import llm

response = llm.invoke(
    """
    You are a cybersecurity analyst.

    Analyze the following log.

    Timestamp: 2026-07-03 10:30
    User: admin
    Event: Failed Login
    IP: 192.168.1.10

    Explain whether this looks suspicious.
    """
)

print(response.content)