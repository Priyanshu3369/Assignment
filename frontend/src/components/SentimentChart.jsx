import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";

const SentimentChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/history?limit=20") // ✅ adjust limit as needed
      .then((res) => res.json())
      .then((history) => {
        // Transform history into chart-friendly format
        const formatted = history.map((entry) => {
          let sentimentScore = 0;
          if (entry.response.text_sentiment === "Positive") sentimentScore = 1;
          if (entry.response.text_sentiment === "Neutral") sentimentScore = 0.5;
          if (entry.response.text_sentiment === "Negative") sentimentScore = 0;

          return {
            id: entry._id,
            timestamp: new Date(entry.timestamp).toLocaleString(),
            sentiment: sentimentScore,
          };
        }).reverse(); // reverse to show oldest → newest

        setData(formatted);
      })
      .catch((err) => console.error("Error fetching history:", err));
  }, []);

  return (
    <div className="sentiment-chart">
      <h3>📊 Sentiment Trend</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" tick={{ fontSize: 12 }} />
          <YAxis domain={[0, 1]} ticks={[0, 0.5, 1]} />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="sentiment" stroke="#8884d8" name="Sentiment Score" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default SentimentChart;
