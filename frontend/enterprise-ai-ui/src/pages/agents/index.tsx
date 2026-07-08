import DashboardLayout from "../../layouts/DashboardLayout";
import { useAgentStore } from "../../store/agentStore";

import AgentCard from "../../components/agents/AgentCard";
import AgentHealth from "../../components/agents/AgentHealth";
import AgentTasks from "../../components/agents/AgentTasks";
import AgentLogs from "../../components/agents/AgentLogs";

const Agents = () => {
  const agents = useAgentStore((state) => state.agents);

  return (
    <DashboardLayout>
      <h1>AI Agents</h1>

      {agents.map((agent) => (
        <AgentCard
          key={agent.id}
          agent={agent}
        />
      ))}

      <AgentHealth />

      <AgentTasks />

      <AgentLogs />
    </DashboardLayout>
  );
};

export default Agents; 