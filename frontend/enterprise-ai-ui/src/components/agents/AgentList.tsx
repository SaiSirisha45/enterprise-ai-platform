import AgentCard from "./AgentCard";

export default function AgentList() {
  const agents = [
    {
      name: "HR Assistant Agent",
      status: "Running" as const,
    },
    {
      name: "Payroll Processing Agent",
      status: "Running" as const,
    },
    {
      name: "Knowledge Retrieval Agent",
      status: "Stopped" as const,
    },
    {
      name: "Analytics Agent",
      status: "Running" as const,
    },
  ];

  return (
    <div>
      {agents.map((agent) => (
        <AgentCard
          key={agent.name}
          name={agent.name}
          status={agent.status}
        />
      ))}
    </div>
  );
} 