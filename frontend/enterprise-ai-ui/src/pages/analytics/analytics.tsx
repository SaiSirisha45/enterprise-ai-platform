import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  {
    name: "Mon",
    workflows: 10,
  },
  {
    name: "Tue",
    workflows: 15,
  },
  {
    name: "Wed",
    workflows: 8,
  },
  {
    name: "Thu",
    workflows: 20,
  },
  {
    name: "Fri",
    workflows: 16,
  },
  {
    name: "Sat",
    workflows: 12,
  },
  {
    name: "Sun",
    workflows: 18,
  },
];

export default function Analytics() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold dark:text-white">
          Analytics Dashboard
        </h1>

        <p className="text-gray-500 dark:text-gray-400">
          Weekly Workflow Activity
        </p>
      </div>

      <div className="rounded-xl bg-white p-6 shadow-md dark:bg-gray-800">
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="name" />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="workflows"
                fill="#2563eb"
                radius={[6, 6, 0, 0]}
              />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
} 