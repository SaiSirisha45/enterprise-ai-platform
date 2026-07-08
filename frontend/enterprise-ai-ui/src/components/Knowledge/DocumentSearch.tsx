import { useState } from "react";

interface DocumentSearchProps {
  onSearch?: (value: string) => void;
}

export default function DocumentSearch({
  onSearch,
}: DocumentSearchProps) {
  const [search, setSearch] = useState("");

  return (
    <div
      style={{
        marginBottom: "20px",
      }}
    >
      <input
        type="text"
        placeholder="Search knowledge documents..."
        value={search}
        onChange={(e) => {
          setSearch(e.target.value);
          onSearch?.(e.target.value);
        }}
        style={{
          width: "100%",
          padding: "12px",
          borderRadius: "8px",
          border: "1px solid #ccc",
          fontSize: "16px",
        }}
      />
    </div>
  );
} 