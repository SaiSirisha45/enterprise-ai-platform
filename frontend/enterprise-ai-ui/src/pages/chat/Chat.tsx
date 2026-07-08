import { useState } from "react";

export default function Chat() {
  const [messages, setMessages] = useState([
    {
      sender: "AI",
      text: "Hello! How can I help you today?",
    },
  ]);

  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;

    setMessages((prev) => [
      ...prev,
      { sender: "You", text: input },
      {
        sender: "AI",
        text: "This is a demo response. Connect your backend AI API here.",
      },
    ]);

    setInput("");
  };

  return (
    <div className="flex h-[80vh] flex-col rounded-xl bg-white shadow dark:bg-gray-800">
      {/* Header */}
      <div className="border-b p-4">
        <h1 className="text-2xl font-bold dark:text-white">
          Enterprise AI Chat
        </h1>
      </div>

      {/* Messages */}
      <div className="flex-1 space-y-4 overflow-y-auto p-4">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`max-w-xl rounded-lg p-3 ${
              msg.sender === "You"
                ? "ml-auto bg-blue-600 text-white"
                : "bg-gray-200 dark:bg-gray-700 dark:text-white"
            }`}
          >
            <p className="text-sm font-semibold">{msg.sender}</p>
            <p>{msg.text}</p>
          </div>
        ))}
      </div>

      {/* Input */}
      <div className="flex gap-2 border-t p-4">
        <input
          type="text"
          placeholder="Ask AI anything..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
          className="flex-1 rounded-lg border px-4 py-2 dark:bg-gray-700 dark:text-white"
        />

        <button
          onClick={sendMessage}
          className="rounded-lg bg-blue-600 px-5 py-2 text-white hover:bg-blue-700"
        >
          Send
        </button>
      </div>
    </div>
  );
} 