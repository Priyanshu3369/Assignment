def generate_response(sentiment: str, topic: str, image_class: str, ocr_text: str, toxicity: float) -> str:
    # Rule 1: Toxicity check
    if toxicity > 0.5:
        return "⚠️ Warning: Toxic or abusive content detected. Please keep the conversation respectful."

    # Rule 2: Negative + restaurant/food complaint
    if sentiment.upper() == "NEGATIVE" and topic in ["Review", "Complaint"] and image_class:
        return "😔 We’re sorry about your negative experience. We’ll investigate and improve."

    # Rule 3: Positive sentiment + product/thing in image
    if sentiment.upper() == "POSITIVE" and topic in ["Review", "Comment"] and image_class:
        return "🎉 Thanks for the positive feedback! Glad you enjoyed this."

    # Rule 4: Neutral feedback
    if sentiment.upper() == "NEUTRAL":
        return "✅ Thanks for your feedback. We’ll take it into consideration."

    # Rule 5: Default fallback
    return "🙏 Thanks for sharing. Your input has been recorded."
