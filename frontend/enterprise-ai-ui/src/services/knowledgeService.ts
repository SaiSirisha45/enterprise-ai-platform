export const uploadDocument = async (file: File) => {
  return {
    id: Date.now(),
    name: file.name,
    type: file.type || "Unknown",
    size: `${(file.size / 1024).toFixed(2)} KB`,
    status: "Uploaded",
  };
}; 