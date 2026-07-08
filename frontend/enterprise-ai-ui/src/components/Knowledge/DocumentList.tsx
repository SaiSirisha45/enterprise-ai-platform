import DocumentCard from "./DocumentCard";

export default function DocumentList() {
  const documents = [
    {
      id: 1,
      name: "Employee Handbook.pdf",
      type: "PDF",
      size: "2.4 MB",
    },
    {
      id: 2,
      name: "Leave Policy.docx",
      type: "DOCX",
      size: "1.2 MB",
    },
    {
      id: 3,
      name: "Company Rules.pdf",
      type: "PDF",
      size: "3.8 MB",
    },
  ];

  return (
    <div>
      {documents.map((document) => (
        <DocumentCard
          key={document.id}
          name={document.name}
          type={document.type}
          size={document.size}
        />
      ))}
    </div>
  );
} 