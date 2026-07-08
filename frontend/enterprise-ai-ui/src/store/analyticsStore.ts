import { create } from "zustand";
import type { AnalyticsData } from "../types/analytics";

interface AnalyticsState {
  data: AnalyticsData;
}

export const useAnalyticsStore = create<AnalyticsState>(() => ({
  data: {
    totalUsers: 120,
    totalChats: 560,
    totalDocuments: 84,
    activeAgents: 5,
  },
})); 