export default function Dashboard() {
  const stats = [
    {
      title: "Running Workflows",
      value: 18,
      color: "text-green-600",
    },
    {
      title: "Failed Workflows",
      value: 2,
      color: "text-red-600",
    },
    {
      title: "Retry Queue",
      value: 5,
      color: "text-yellow-600",
    },
    {
      title: "Active AI Agents",
      value: 9,
      color: "text-blue-600",
    },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold dark:text-white">
          Enterprise Dashboard
        </h1>

        <p className="text-gray-500 dark:text-gray-400">
          Welcome to your AI Workspace
        </p>
      </div>

      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {stats.map((card) => (
          <div
            key={card.title}
            className="rounded-xl bg-white p-6 shadow-md dark:bg-gray-800"
          >
            <h2 className="text-gray-500 dark:text-gray-400">
              {card.title}
            </h2>

            <p className={`mt-3 text-4xl font-bold ${card.color}`}>
              {card.value}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}