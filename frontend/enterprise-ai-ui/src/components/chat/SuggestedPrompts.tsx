interface SuggestedPromptsProps {
  onSelect?: (prompt: string) => void;
}

export default function SuggestedPrompts({
  onSelect,
}: SuggestedPromptsProps) {
  const prompts = [
    "Show employee leave balance",
    "List all active AI agents",
    "Upload a knowledge document",
    "Show today's analytics",
  ];

  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        flexWrap: "wrap",
        padding: "15px 20px",
        background: "#f8f9fa",
        borderTop: "1px solid #ddd",
      }}
    >
      {prompts.map((prompt) => (
        <button
          key={prompt}
          onClick={() => onSelect?.(prompt)}
          style={{
            padding: "10px 14px",
            border: "1px solid #2563eb",
            borderRadius: "20px",
            background: "#ffffff",
            color: "#2563eb",
            cursor: "pointer",
          }}
        >
          {prompt}
        </button>
      ))}
    </div>
  );
} 