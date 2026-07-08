import api from "./axios";

export const getAgents = async () => {
  const response = await api.get("/agents");
  return response.data;
};

export const startAgent = async (id: string) => {
  const response = await api.post(`/agents/${id}/start`);
  return response.data;
};

export const stopAgent = async (id: string) => {
  const response = await api.post(`/agents/${id}/stop`);
  return response.data;
};