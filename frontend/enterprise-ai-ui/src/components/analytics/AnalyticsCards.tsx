import { useAnalyticsStore } from "../../store/analyticsStore";

const AnalyticsCards = () => {
  const data = useAnalyticsStore((state) => state.data);

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(4, 1fr)",
        gap: "20px",
        marginBottom: "30px",
      }}
    >
      <div style={{ border: "1px solid #ddd", padding: "20px" }}>
        <h3>Users</h3>
        <h2>{data.totalUsers}</h2>
      </div>

      <div style={{ border: "1px solid #ddd", padding: "20px" }}>
        <h3>Chats</h3>
        <h2>{data.totalChats}</h2>
      </div>

      <div style={{ border: "1px solid #ddd", padding: "20px" }}>
        <h3>Documents</h3>
        <h2>{data.totalDocuments}</h2>
      </div>

      <div style={{ border: "1px solid #ddd", padding: "20px" }}>
        <h3>Agents</h3>
        <h2>{data.activeAgents}</h2>
      </div>
    </div>
  );
};

export default AnalyticsCards; 