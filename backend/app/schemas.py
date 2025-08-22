from pydantic import BaseModel
from typing import Optional, Dict

# Input schema
class AnalyzeRequest(BaseModel):
    text: str
    image_base64: Optional[str] = None

# Output schema
class AnalyzeResponse(BaseModel):
    text_sentiment: str
    text_summary: Optional[str] = None
    topic: Optional[str] = None
    image_classification: Optional[str] = None
    ocr_text: Optional[str] = None
    toxicity_score: Optional[float] = None
    automated_response: str
    flags: Dict[str, bool] = {}
