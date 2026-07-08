import { useChatStore } from "../../store/chatStore";
import ChatMessage from "./ChatMessage";

const ChatWindow = () => {
  const messages = useChatStore((state) => state.messages);

  return (
    <div
      style={{
        flex: 1,
        padding: "20px",
        overflowY: "auto",
        background: "#f8fafc",
      }}
    >
      {messages.length === 0 ? (
        <h3>Start a conversation with AI</h3>
      ) : (
        messages.map((message) => (
          <ChatMessage key={message.id} message={message} />
        ))
      )}
    </div>
  );
};

export default ChatWindow; 