import DashboardCard from "./DashboardCard";

export default function Statistics() {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
        gap: "20px",
        marginBottom: "30px",
      }}
    >
      <DashboardCard
        title="Active Users"
        value={156}
        color="#10b981"
      />

      <DashboardCard
        title="Running Agents"
        value={12}
        color="#3b82f6"
      />

      <DashboardCard
        title="Knowledge Documents"
        value={2340}
        color="#f59e0b"
      />

      <DashboardCard
        title="Today's AI Queries"
        value={8420}
        color="#ef4444"
      />
    </div>
  );
} 