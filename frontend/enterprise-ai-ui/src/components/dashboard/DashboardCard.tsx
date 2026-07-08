interface DashboardCardProps {
  title: string;
  value: string | number;
  color?: string;
}

export default function DashboardCard({
  title,
  value,
  color = "#2563eb",
}: DashboardCardProps) {
  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "12px",
        padding: "20px",
        boxShadow: "0 2px 10px rgba(0,0,0,0.08)",
        borderLeft: `6px solid ${color}`,
        minHeight: "120px",
      }}
    >
      <h3
        style={{
          margin: 0,
          color: "#555",
          fontSize: "16px",
        }}
      >
        {title}
      </h3>

      <h1
        style={{
          marginTop: "15px",
          fontSize: "32px",
          color: color,
        }}
      >
        {value}
      </h1>
    </div>
  );
} 