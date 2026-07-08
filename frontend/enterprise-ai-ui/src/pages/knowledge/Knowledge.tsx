import { useMemo, useState } from "react";

const documents = [
  {
    id: 1,
    name: "Employee Handbook.pdf",
    category: "HR",
    status: "Indexed",
  },
  {
    id: 2,
    name: "Leave Policy.pdf",
    category: "HR",
    status: "Processing",
  },
  {
    id: 3,
    name: "Payroll Guide.pdf",
    category: "Finance",
    status: "Indexed",
  },
  {
    id: 4,
    name: "Project SOP.pdf",
    category: "Engineering",
    status: "Indexed",
  },
];

export default function Knowledge() {
  const [search, setSearch] = useState("");

  const filtered = useMemo(() => {
    return documents.filter(
      (doc) =>
        doc.name.toLowerCase().includes(search.toLowerCase()) ||
        doc.category.toLowerCase().includes(search.toLowerCase())
    );
  }, [search]);

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h1 className="text-3xl font-bold dark:text-white">
            Knowledge Base
          </h1>
          <p className="text-gray-500 dark:text-gray-400">
            Manage enterprise documents
          </p>
        </div>

        <button className="rounded-lg bg-blue-600 px-5 py-2 text-white hover:bg-blue-700">
          Upload Document
        </button>
      </div>

      <input
        type="text"
        placeholder="Search documents..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="w-full rounded-lg border px-4 py-2 dark:bg-gray-800 dark:text-white"
      />

      <div className="overflow-x-auto rounded-xl bg-white shadow dark:bg-gray-800">
        <table className="min-w-full">
          <thead className="border-b bg-gray-100 dark:bg-gray-700">
            <tr>
              <th className="px-4 py-3 text-left">Document</th>
              <th className="px-4 py-3 text-left">Category</th>
              <th className="px-4 py-3 text-left">Status</th>
            </tr>
          </thead>

          <tbody>
            {filtered.map((doc) => (
              <tr
                key={doc.id}
                className="border-b hover:bg-gray-50 dark:hover:bg-gray-700"
              >
                <td className="px-4 py-3">{doc.name}</td>

                <td className="px-4 py-3">{doc.category}</td>

                <td className="px-4 py-3">
                  <span
                    className={`rounded-full px-3 py-1 text-sm ${
                      doc.status === "Indexed"
                        ? "bg-green-100 text-green-700"
                        : "bg-yellow-100 text-yellow-700"
                    }`}
                  >
                    {doc.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
} 