from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class AnalyzeRequest(BaseModel):
    text: str
    image_base64: Optional[str] = None

class AnalyzeResponse(BaseModel):
    text_sentiment: str
    text_summary: str
    topic: str
    image_classification: Optional[str]
    ocr_text: Optional[str]
    toxicity_score: float
    automated_response: str
    flags: Dict[str, bool]

class HistoryEntry(BaseModel):
    text: str
    image_base64: Optional[str]
    response: dict
    timestamp: datetime
