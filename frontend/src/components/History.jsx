import React, { useEffect, useState } from "react";
import { getHistory } from "../api";

const History = () => {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const data = await getHistory();
        setHistory(data);
      } catch (err) {
        console.error("Error fetching history", err);
      } finally {
        setLoading(false);
      }
    };
    fetchHistory();
  }, []);

  if (loading) return <p>Loading history...</p>;

  return (
    <div className="history">
      <h3>🕘 Conversation History</h3>
      {history.length === 0 ? (
        <p>No past records</p>
      ) : (
        <ul>
          {history.map((item) => (
            <li key={item._id} className="history-item">
              <p><b>Text:</b> {item.text}</p>
              <p><b>Sentiment:</b> {item.text_sentiment}</p>
              <p><b>Topic:</b> {item.topic}</p>
              <p><b>Response:</b> {item.automated_response}</p>
              <hr />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default History;
