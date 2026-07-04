from pydantic import BaseModel


class LogRequest(BaseModel):
    logs: list


class AnalysisResponse(BaseModel):
    status: str
    result: dict