from detoxify import Detoxify

# Load once at startup
toxicity_model = Detoxify('original')

def check_toxicity(text: str) -> float:
    if not text or text.strip() == "":
        return 0.0
    result = toxicity_model.predict(text)
    # "toxicity" key is the main score
    return float(result["toxicity"])
