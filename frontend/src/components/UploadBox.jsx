import React, { useState } from "react";
import { analyzeData } from "../api";

const UploadBox = ({ setResult }) => {
  const [text, setText] = useState("");
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const data = await analyzeData(text, image);
      setResult(data);
    } catch (err) {
      alert("Error analyzing data");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-box">
      <textarea
        placeholder="Enter text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <input
        type="file"
        accept="image/*"
        onChange={(e) => setImage(e.target.files[0])}
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
};

export default UploadBox;
