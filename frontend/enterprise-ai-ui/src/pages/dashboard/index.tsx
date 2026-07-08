import DashboardHeader from "../../components/dashboard/DashboardHeader";
import Statistics from "../../components/dashboard/Statistics";
import RecentActivity from "../../components/dashboard/RecentActivity";

export default function Dashboard() {
  return (
    <div
      style={{
        padding: "30px",
        background: "#f5f7fb",
        minHeight: "100vh",
      }}
    >
      <DashboardHeader userName="Demo User" />

      <Statistics />

      <RecentActivity />
    </div>
  );
} 