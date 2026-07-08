const users = [
  {
    id: 1,
    name: "Sai Sirisha",
    role: "Admin",
    status: "Active",
  },
  {
    id: 2,
    name: "John Smith",
    role: "Manager",
    status: "Active",
  },
  {
    id: 3,
    name: "Alice Johnson",
    role: "Employee",
    status: "Inactive",
  },
  {
    id: 4,
    name: "Rahul Kumar",
    role: "AI Engineer",
    status: "Active",
  },
];

export default function Admin() {
  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold dark:text-white">
          Admin Dashboard
        </h1>

        <p className="text-gray-500 dark:text-gray-400">
          Manage enterprise users and roles
        </p>
      </div>

      {/* Summary Cards */}
      <div className="grid gap-6 md:grid-cols-3">
        <div className="rounded-xl bg-white p-6 shadow dark:bg-gray-800">
          <h2 className="text-gray-500 dark:text-gray-400">
            Total Users
          </h2>

          <p className="mt-2 text-4xl font-bold text-blue-600">
            245
          </p>
        </div>

        <div className="rounded-xl bg-white p-6 shadow dark:bg-gray-800">
          <h2 className="text-gray-500 dark:text-gray-400">
            Active Users
          </h2>

          <p className="mt-2 text-4xl font-bold text-green-600">
            231
          </p>
        </div>

        <div className="rounded-xl bg-white p-6 shadow dark:bg-gray-800">
          <h2 className="text-gray-500 dark:text-gray-400">
            AI Agents
          </h2>

          <p className="mt-2 text-4xl font-bold text-purple-600">
            9
          </p>
        </div>
      </div>

      {/* Users Table */}
      <div className="overflow-x-auto rounded-xl bg-white shadow dark:bg-gray-800">
        <table className="min-w-full">
          <thead className="bg-gray-100 dark:bg-gray-700">
            <tr>
              <th className="px-4 py-3 text-left">Name</th>
              <th className="px-4 py-3 text-left">Role</th>
              <th className="px-4 py-3 text-left">Status</th>
              <th className="px-4 py-3 text-left">Action</th>
            </tr>
          </thead>

          <tbody>
            {users.map((user) => (
              <tr
                key={user.id}
                className="border-b hover:bg-gray-50 dark:hover:bg-gray-700"
              >
                <td className="px-4 py-3">{user.name}</td>

                <td className="px-4 py-3">{user.role}</td>

                <td className="px-4 py-3">
                  <span
                    className={`rounded-full px-3 py-1 text-sm ${
                      user.status === "Active"
                        ? "bg-green-100 text-green-700"
                        : "bg-red-100 text-red-700"
                    }`}
                  >
                    {user.status}
                  </span>
                </td>

                <td className="px-4 py-3">
                  <button className="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
                    Manage
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
} 