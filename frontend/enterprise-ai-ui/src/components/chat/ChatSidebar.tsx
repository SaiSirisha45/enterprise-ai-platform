const ChatSidebar = () => {
  return (
    <div
      style={{
        width: "260px",
        background: "#1e293b",
        color: "white",
        padding: "20px",
      }}
    >
      <h2>Chats</h2>

      <button
        style={{
          marginTop: "20px",
          width: "100%",
          padding: "10px",
        }}
      >
        + New Chat
      </button>
    </div>
  );
};

export default ChatSidebar; 