import type { ChangeEvent } from "react";
import { uploadDocument } from "../../services/knowledgeService";
import { useKnowledgeStore } from "../../store/knowledgeStore";

const DocumentUpload = () => {
  const addDocument = useKnowledgeStore((state) => state.addDocument);

  const handleUpload = async (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];

    if (!file) return;

    const document = await uploadDocument(file);
    addDocument(document);
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        type="file"
        accept=".pdf,.doc,.docx,.txt,.md"
        onChange={handleUpload}
      />
    </div>
  );
};

export default DocumentUpload; 