const workflows = [
  {
    id: 1,
    name: "Employee Onboarding",
    status: "Running",
    owner: "HR",
  },
  {
    id: 2,
    name: "Payroll Processing",
    status: "Completed",
    owner: "Finance",
  },
  {
    id: 3,
    name: "Leave Approval",
    status: "Failed",
    owner: "HR",
  },
  {
    id: 4,
    name: "Project Assignment",
    status: "Running",
    owner: "Engineering",
  },
];

export default function Workflows() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold dark:text-white">
          Enterprise Workflows
        </h1>

        <p className="text-gray-500 dark:text-gray-400">
          Monitor and manage workflow execution
        </p>
      </div>

      <div className="overflow-x-auto rounded-xl bg-white shadow-md dark:bg-gray-800">
        <table className="min-w-full">
          <thead className="border-b bg-gray-100 dark:bg-gray-700">
            <tr>
              <th className="px-4 py-3 text-left">Workflow</th>
              <th className="px-4 py-3 text-left">Owner</th>
              <th className="px-4 py-3 text-left">Status</th>
              <th className="px-4 py-3 text-left">Action</th>
            </tr>
          </thead>

          <tbody>
            {workflows.map((workflow) => (
              <tr
                key={workflow.id}
                className="border-b hover:bg-gray-50 dark:hover:bg-gray-700"
              >
                <td className="px-4 py-3">{workflow.name}</td>

                <td className="px-4 py-3">{workflow.owner}</td>

                <td className="px-4 py-3">
                  <span
                    className={`rounded-full px-3 py-1 text-sm ${
                      workflow.status === "Completed"
                        ? "bg-green-100 text-green-700"
                        : workflow.status === "Running"
                        ? "bg-blue-100 text-blue-700"
                        : "bg-red-100 text-red-700"
                    }`}
                  >
                    {workflow.status}
                  </span>
                </td>

                <td className="px-4 py-3">
                  <button className="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
                    View
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