import React, { useEffect, useState } from "react";

const ConversationHistory = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/history?limit=20")
      .then((res) => res.json())
      .then((data) => setHistory(data.reverse())) // oldest → newest
      .catch((err) => console.error("Error fetching history:", err));
  }, []);

  return (
    <div className="conversation-history">
      <h3>💬 Conversation History</h3>
      <div className="chat-window">
        {history.map((entry) => (
          <div key={entry._id} className="chat-entry">
            {/* --- User message --- */}
            <div className="chat-bubble user-bubble">
              <p><b>User:</b> {entry.text}</p>
              {entry.image_base64 && (
                <img
                  src={`data:image/jpeg;base64,${entry.image_base64}`}
                  alt="User Upload"
                  style={{ maxWidth: "150px", borderRadius: "8px", marginTop: "5px" }}
                />
              )}
            </div>

            {/* --- Bot response --- */}
            <div className="chat-bubble bot-bubble">
              <p><b>Bot:</b> {entry.response.automated_response}</p>
              <small>
                Sentiment: {entry.response.text_sentiment} | 
                Topic: {entry.response.topic}
              </small>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ConversationHistory;
