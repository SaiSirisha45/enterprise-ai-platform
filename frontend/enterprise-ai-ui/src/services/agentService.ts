export const fetchAgents = async () => {
  return [
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
  ];
}; 