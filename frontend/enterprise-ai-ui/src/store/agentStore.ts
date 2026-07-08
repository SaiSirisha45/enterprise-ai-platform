import { create } from "zustand";
import type { Agent } from "../types/agent";

interface AgentState {
  agents: Agent[];

  startAgent: (id: number) => void;
  stopAgent: (id: number) => void;
  restartAgent: (id: number) => void;
}

export const useAgentStore = create<AgentState>((set) => ({
  agents: [
    {
      id: 1,
      name: "Research Agent",
      status: "Running",
      health: "Healthy",
    },
    {
      id: 2,
      name: "RAG Agent",
      status: "Stopped",
      health: "Warning",
    },
  ],

  startAgent: (id) =>
    set((state) => ({
      agents: state.agents.map((agent) =>
        agent.id === id
          ? { ...agent, status: "Running" }
          : agent
      ),
    })),

  stopAgent: (id) =>
    set((state) => ({
      agents: state.agents.map((agent) =>
        agent.id === id
          ? { ...agent, status: "Stopped" }
          : agent
      ),
    })),

  restartAgent: (id) =>
    set((state) => ({
      agents: state.agents.map((agent) =>
        agent.id === id
          ? { ...agent, status: "Running" }
          : agent
      ),
    })),
})); 