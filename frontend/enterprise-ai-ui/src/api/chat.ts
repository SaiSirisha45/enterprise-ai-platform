import api from "./axios";

export const getChatHistory = async () => {
  const response = await api.get("/chat/history");
  return response.data;
};

export const sendMessage = async (message: string) => {
  const response = await api.post("/chat", {
    message,
  });

  return response.data;
};