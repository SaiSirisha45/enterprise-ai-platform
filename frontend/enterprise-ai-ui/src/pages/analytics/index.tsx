import DashboardLayout from "../../layouts/DashboardLayout";
import AnalyticsCards from "../../components/analytics/AnalyticsCards";
import UsageChart from "../../components/analytics/UsageChart";
import AgentPerformance from "../../components/analytics/AgentPerformance";
import ChatAnalytics from "../../components/analytics/ChatAnalytics";
import DocumentAnalytics from "../../components/analytics/DocumentAnalytics";

const Analytics = () => {
  return (
    <DashboardLayout>
      <h1>Analytics Dashboard</h1>

      <AnalyticsCards />

      <UsageChart />

      <AgentPerformance />

      <ChatAnalytics />

      <DocumentAnalytics />
    </DashboardLayout>
  );
};

export default Analytics; 