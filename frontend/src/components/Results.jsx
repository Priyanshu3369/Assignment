import React from "react";

const Results = ({ result }) => {
  if (!result) return null;

  return (
    <div className="results">
      <h3>Analysis Results</h3>
      <p><b>Sentiment:</b> {result.text_sentiment}</p>
      <p><b>Summary:</b> {result.text_summary}</p>
      <p><b>Topic:</b> {result.topic}</p>
      <p><b>Image Classification:</b> {result.image_classification || "N/A"}</p>
      <p><b>OCR Text:</b> {result.ocr_text || "N/A"}</p>
      <p><b>Toxicity Score:</b> {(result.toxicity_score * 100).toFixed(1)}%</p>
      <p><b>Response:</b> {result.automated_response}</p>
    </div>
  );
};

export default Results;
