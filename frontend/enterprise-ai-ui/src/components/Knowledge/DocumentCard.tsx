interface DocumentCardProps {
  name: string;
  type: string;
  size: string;
}

export default function DocumentCard({
  name,
  type,
  size,
}: DocumentCardProps) {
  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "10px",
        padding: "20px",
        marginBottom: "15px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
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
            margin: "8px 0 0",
            color: "#666",
          }}
        >
          {type} • {size}
        </p>
      </div>

      <button
        style={{
          padding: "8px 16px",
          background: "#ef4444",
          color: "#fff",
          border: "none",
          borderRadius: "6px",
          cursor: "pointer",
        }}
      >
        Delete
      </button>
    </div>
  );
} 