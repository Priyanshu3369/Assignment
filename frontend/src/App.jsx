import React, { useState } from "react";
import UploadBox from "./components/UploadBox.jsx";
import Results from "./components/Results.jsx";
import SentimentChart from "./components/SentimentChart.jsx";
import ConversationHistory from "./components/ConversationHistory.jsx";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="App">
      <h1>📊 Multimodal Analyzer</h1>
      <UploadBox setResult={setResult} />
      <Results result={result} />
      <SentimentChart />
      <ConversationHistory />
    </div>
  );
}

export default App;
