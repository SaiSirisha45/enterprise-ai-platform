export default function ChatMessages() {
  const messages = [
    {
      sender: "AI",
      text: "Hello! How can I help you today?",
    },
    {
      sender: "You",
      text: "Show me employee leave balance.",
    },
    {
      sender: "AI",
      text: "Employee leave balance has been retrieved successfully.",
    },
  ];

  return (
    <div
      style={{
        flex: 1,
        padding: "20px",
        overflowY: "auto",
        background: "#f8f9fa",
      }}
    >
      {messages.map((message, index) => (
        <div
          key={index}
          style={{
            display: "flex",
            justifyContent:
              message.sender === "You"
                ? "flex-end"
                : "flex-start",
            marginBottom: "15px",
          }}
        >
          <div
            style={{
              background:
                message.sender === "You"
                  ? "#2563eb"
                  : "#ffffff",
              color:
                message.sender === "You"
                  ? "#ffffff"
                  : "#000000",
              padding: "12px 16px",
              borderRadius: "12px",
              maxWidth: "70%",
              boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
            }}
          >
            <strong>{message.sender}</strong>
            <br />
            {message.text}
          </div>
        </div>
      ))}
    </div>
  );
} 