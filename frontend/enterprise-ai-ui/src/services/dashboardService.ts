import api from "./api";

// Dashboard Statistics
export const getDashboardStats = async () => {
  try {
    const response = await api.get("/dashboard/stats");
    return response.data;
  } catch (error) {
    console.error("Error fetching dashboard stats:", error);
    throw error;
  }
};

// Recent Activities
export const getRecentActivities = async () => {
  try {
    const response = await api.get("/dashboard/activities");
    return response.data;
  } catch (error) {
    console.error("Error fetching recent activities:", error);
    throw error;
  }
};

// AI Agent Status
export const getAgentStatus = async () => {
  try {
    const response = await api.get("/dashboard/agents");
    return response.data;
  } catch (error) {
    console.error("Error fetching agent status:", error);
    throw error;
  }
};

// Workflow Summary
export const getWorkflowSummary = async () => {
  try {
    const response = await api.get("/dashboard/workflows");
    return response.data;
  } catch (error) {
    console.error("Error fetching workflow summary:", error);
    throw error;
  }
}; 