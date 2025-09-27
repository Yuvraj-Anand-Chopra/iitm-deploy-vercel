from pydantic import BaseModel
from typing import List

class LatencyData(BaseModel):
    region: str
    service: str
    latency_ms: float
    uptime_pct: float
    timestamp: int

class LatencyResponse(BaseModel):
    data: List[LatencyData]