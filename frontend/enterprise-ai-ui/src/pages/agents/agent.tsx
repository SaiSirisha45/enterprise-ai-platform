const agents = [
  {
    id: 1,
    name: "HR Assistant",
    description: "Answers HR policy and employee questions.",
    status: "Online",
  },
  {
    id: 2,
    name: "Knowledge Agent",
    description: "Searches enterprise documents using RAG.",
    status: "Online",
  },
  {
    id: 3,
    name: "Workflow Agent",
    description: "Automates enterprise workflows.",
    status: "Busy",
  },
  {
    id: 4,
    name: "Analytics Agent",
    description: "Generates reports and dashboards.",
    status: "Offline",
  },
];

export default function Agents() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold dark:text-white">
          AI Agents
        </h1>

        <p className="text-gray-500 dark:text-gray-400">
          Manage and monitor enterprise AI agents
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        {agents.map((agent) => (
          <div
            key={agent.id}
            className="rounded-xl bg-white p-6 shadow-md dark:bg-gray-800"
          >
            <h2 className="text-xl font-semibold dark:text-white">
              {agent.name}
            </h2>

            <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
              {agent.description}
            </p>

            <div className="mt-4">
              <span
                className={`rounded-full px-3 py-1 text-sm ${
                  agent.status === "Online"
                    ? "bg-green-100 text-green-700"
                    : agent.status === "Busy"
                    ? "bg-yellow-100 text-yellow-700"
                    : "bg-red-100 text-red-700"
                }`}
              >
                {agent.status}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
} 