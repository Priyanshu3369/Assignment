import React, { useState } from "react";
import UploadBox from "./components/UploadBox.jsx";
import Results from "./components/Results.jsx";
import History from "./components/History.jsx";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="App">
      <h1>📊 Multimodal Analyzer</h1>
      <UploadBox setResult={setResult} />
      <Results result={result} />
      <History />
    </div>
  );
}

export default App;
