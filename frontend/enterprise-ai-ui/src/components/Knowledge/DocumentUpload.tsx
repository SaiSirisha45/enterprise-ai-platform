import { useState } from "react";

export default function DocumentUpload() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleUpload = () => {
    if (!selectedFile) {
      alert("Please select a document.");
      return;
    }

    alert(`Uploading: ${selectedFile.name}`);

    // Later we'll call the backend upload API here.
  };

  return (
    <div
      style={{
        padding: "20px",
        border: "2px dashed #ccc",
        borderRadius: "10px",
        marginBottom: "20px",
        background: "#ffffff",
      }}
    >
      <h3>Upload Knowledge Document</h3>

      <input
        type="file"
        onChange={(e) => {
          if (e.target.files?.length) {
            setSelectedFile(e.target.files[0]);
          }
        }}
      />

      <br />
      <br />

      <button
        onClick={handleUpload}
        style={{
          padding: "10px 18px",
          background: "#2563eb",
          color: "#fff",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
        }}
      >
        Upload
      </button>

      {selectedFile && (
        <p style={{ marginTop: "10px" }}>
          Selected File: <strong>{selectedFile.name}</strong>
        </p>
      )}
    </div>
  );
} 