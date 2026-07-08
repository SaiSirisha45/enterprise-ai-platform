import { useState } from "react";

export default function ChatInput() {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (!message.trim()) return;

    alert(`Message Sent: ${message}`);

    setMessage("");
  };

  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        padding: "20px",
        borderTop: "1px solid #ddd",
        background: "#ffffff",
      }}
    >
      <input
        type="text"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          flex: 1,
          padding: "12px",
          borderRadius: "8px",
          border: "1px solid #ccc",
        }}
      />

      <button
        onClick={handleSend}
        style={{
          padding: "12px 20px",
          border: "none",
          borderRadius: "8px",
          background: "#2563eb",
          color: "#fff",
          cursor: "pointer",
        }}
      >
        Send
      </button>
    </div>
  );
} 