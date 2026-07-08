interface DashboardHeaderProps {
  userName: string;
}

export default function DashboardHeader({
  userName,
}: DashboardHeaderProps) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "30px",
      }}
    >
      <div>
        <h1
          style={{
            margin: 0,
            fontSize: "30px",
          }}
        >
          Enterprise AI Dashboard
        </h1>

        <p
          style={{
            color: "#666",
            marginTop: "8px",
          }}
        >
          Monitor AI usage, agents, workflows and analytics.
        </p>
      </div>

      <div
        style={{
          fontWeight: "bold",
          fontSize: "18px",
        }}
      >
        Welcome, {userName}
      </div>
    </div>
  );
} 