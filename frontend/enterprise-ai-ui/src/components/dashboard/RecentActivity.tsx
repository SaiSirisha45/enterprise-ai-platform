export default function RecentActivity() {
  const activities = [
    "🤖 HR Agent processed 24 employee requests",
    "📄 12 new knowledge documents uploaded",
    "💬 AI Chat answered 152 questions",
    "⚙️ Workflow 'Leave Approval' completed",
    "👤 New Admin user created",
  ];

  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "12px",
        padding: "20px",
        boxShadow: "0 2px 10px rgba(0,0,0,0.08)",
      }}
    >
      <h2
        style={{
          marginBottom: "20px",
        }}
      >
        Recent Activity
      </h2>

      {activities.map((activity, index) => (
        <div
          key={index}
          style={{
            padding: "12px 0",
            borderBottom:
              index !== activities.length - 1
                ? "1px solid #eee"
                : "none",
          }}
        >
          {activity}
        </div>
      ))}
    </div>
  );
} 