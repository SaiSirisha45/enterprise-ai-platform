import api from "./axios";

export const getWorkflowHistory = async () => {
  const response = await api.get("/workflow/history");
  return response.data;
};

export const retryWorkflow = async (id: string) => {
  const response = await api.post(`/workflow/retry/${id}`);
  return response.data;
};