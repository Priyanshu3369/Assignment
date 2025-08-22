from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import AnalyzeRequest, AnalyzeResponse
from .pipelines import nlp, vision, toxicity, fusion

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

    # --- NLP ---
    sentiment = nlp.analyze_sentiment(payload.text)
    summary = nlp.summarize_text(payload.text)
    topic = nlp.classify_topic(payload.text)

    # --- CV ---
    image_classification, ocr_text = None, None
    if payload.image_base64:
        try:
            img = vision.load_image_from_base64(payload.image_base64)
            image_classification = vision.classify_image(img)
            ocr_text = vision.extract_text(img)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Image processing failed: {str(e)}")

    # --- Toxicity ---
    text_toxicity = toxicity.check_toxicity(payload.text)
    ocr_toxicity = toxicity.check_toxicity(ocr_text)
    final_toxicity = max(text_toxicity, ocr_toxicity)

    # --- Fusion (smart response) ---
    auto_response = fusion.generate_response(
        sentiment=sentiment,
        topic=topic,
        image_class=image_classification,
        ocr_text=ocr_text,
        toxicity=final_toxicity
    )

    return AnalyzeResponse(
        text_sentiment=sentiment,
        text_summary=summary,
        topic=topic,
        image_classification=image_classification,
        ocr_text=ocr_text,
        toxicity_score=final_toxicity,
        automated_response=auto_response,
        flags={"toxic": final_toxicity > 0.5}
    )
