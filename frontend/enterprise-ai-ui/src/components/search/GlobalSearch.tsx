import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";

const pages = [
  { name: "Dashboard", path: "/dashboard" },
  { name: "AI Chat", path: "/chat" },
  { name: "Knowledge Base", path: "/knowledge" },
  { name: "Agents", path: "/agents" },
  { name: "Workflows", path: "/workflows" },
  { name: "Analytics", path: "/analytics" },
  { name: "Admin", path: "/admin" },
  { name: "Settings", path: "/settings" },
  { name: "Profile", path: "/profile" },
];

export default function GlobalSearch() {
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);
  const navigate = useNavigate();

  const results = useMemo(() => {
    if (!query.trim()) return [];
    return pages.filter((page) =>
      page.name.toLowerCase().includes(query.toLowerCase())
    );
  }, [query]);

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      // Ctrl + K (Windows/Linux) or Cmd + K (Mac)
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        inputRef.current?.focus();
      }

      // Escape clears the search
      if (event.key === "Escape") {
        setQuery("");
        inputRef.current?.blur();
      }
    };

    window.addEventListener("keydown", handleKeyDown);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  return (
    <div className="relative w-72">
      <input
        ref={inputRef}
        type="text"
        placeholder="Search... (Ctrl + K)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="w-full rounded-md border border-gray-300 bg-white px-3 py-2 pr-16 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:border-gray-700 dark:bg-gray-800 dark:text-white"
      />

      <span className="absolute right-3 top-2 text-xs text-gray-500">
        Ctrl + K
      </span>

      {results.length > 0 && (
        <div className="absolute z-50 mt-2 w-full rounded-md border border-gray-200 bg-white shadow-lg dark:border-gray-700 dark:bg-gray-800">
          {results.map((page) => (
            <button
              key={page.path}
              onClick={() => {
                navigate(page.path);
                setQuery("");
              }}
              className="block w-full px-4 py-2 text-left hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              {page.name}
            </button>
          ))}
        </div>
      )}
    </div>
  );
} 