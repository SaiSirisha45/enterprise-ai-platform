interface AgentCardProps {
  name: string;
  status: "Running" | "Stopped";
}

export default function AgentCard({
  name,
  status,
}: AgentCardProps) {
  return (
    <div
      style={{
        background: "#fff",
        borderRadius: "12px",
        padding: "20px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "15px",
      }}
    >
      <div>
        <h3
          style={{
            margin: 0,
          }}
        >
          {name}
        </h3>

        <p
          style={{
            color: status === "Running" ? "green" : "red",
            fontWeight: "bold",
            marginTop: "8px",
          }}
        >
          ● {status}
        </p>
      </div>

      <div
        style={{
          display: "flex",
          gap: "10px",
        }}
      >
        <button
          style={{
            padding: "8px 16px",
            background: "#16a34a",
            color: "#fff",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
          }}
        >
          Start
        </button>

        <button
          style={{
            padding: "8px 16px",
            background: "#dc2626",
            color: "#fff",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
          }}
        >
          Stop
        </button>
      </div>
    </div>
  );
} 