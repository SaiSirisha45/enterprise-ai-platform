import api from "./axios";

export const getDocuments = async () => {
  const response = await api.get("/knowledge");
  return response.data;
};

export const uploadDocument = async (formData: FormData) => {
  const response = await api.post("/knowledge/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export const deleteDocument = async (id: string) => {
  const response = await api.delete(`/knowledge/${id}`);
  return response.data;
};