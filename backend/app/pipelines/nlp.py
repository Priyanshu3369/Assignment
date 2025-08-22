from transformers import pipeline

# Load pipelines once at startup
sentiment_pipeline = pipeline("sentiment-analysis")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
topic_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Candidate labels for topic classification
CANDIDATE_TOPICS = ["News", "Review", "Comment", "Support", "Complaint", "Question"]

def analyze_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)[0]
    return result["label"]  # Positive / Negative / Neutral (sometimes only Pos/Neg)

def summarize_text(text: str) -> str:
    if len(text.split()) < 18:  # short text doesn't need summary
        return None
    result = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return result[0]["summary_text"]

def classify_topic(text: str) -> str:
    result = topic_classifier(text, candidate_labels=CANDIDATE_TOPICS)
    return result["labels"][0]  # best topic
