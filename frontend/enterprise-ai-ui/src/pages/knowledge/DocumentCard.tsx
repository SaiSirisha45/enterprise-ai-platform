import type { Document } from "../../types/knowledge";
import { useKnowledgeStore } from "../../store/knowledgeStore";

interface Props {
  document: Document;
}

const DocumentCard = ({ document }: Props) => {
  const deleteDocument = useKnowledgeStore(
    (state) => state.deleteDocument
  );

  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "15px",
        marginBottom: "10px",
        borderRadius: "8px",
      }}
    >
      <h3>{document.name}</h3>

      <p>Type: {document.type}</p>

      <p>Size: {document.size}</p>

      <p>Status: {document.status}</p>

      <button onClick={() => deleteDocument(document.id)}>
        Delete
      </button>
    </div>
  );
};

export default DocumentCard; 