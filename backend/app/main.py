from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import AnalyzeRequest, AnalyzeResponse
from .pipelines import nlp

app = FastAPI(title="Multimodal Analyzer")

# Enable CORS (so frontend can call backend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(payload: AnalyzeRequest):
    if not payload.text:
        raise HTTPException(status_code=400, detail="Text is required")

    # NLP Analysis
    sentiment = nlp.analyze_sentiment(payload.text)
    summary = nlp.summarize_text(payload.text)
    topic = nlp.classify_topic(payload.text)

    # Stub CV + toxicity for now
    return AnalyzeResponse(
        text_sentiment=sentiment,
        text_summary=summary,
        topic=topic,
        image_classification=None,
        ocr_text=None,
        toxicity_score=None,
        automated_response=f"Detected sentiment: {sentiment}",
        flags={}
    )
