import { useKnowledgeStore } from "../../store/knowledgeStore";
import DocumentCard from "./DocumentCard";

const DocumentList = () => {
  const documents = useKnowledgeStore((state) => state.documents);

  if (documents.length === 0) {
    return <h3>No documents uploaded.</h3>;
  }

  return (
    <div>
      {documents.map((document) => (
        <DocumentCard
          key={document.id}
          document={document}
        />
      ))}
    </div>
  );
};

export default DocumentList; 