import { useQuery } from "@tanstack/react-query";
import { getDashboard } from "../../api/dashboard";

export default function Dashboard() {
  const {
    data,
    isLoading,
    isError,
  } = useQuery({
    queryKey: ["dashboard"],
    queryFn: async () => {
      const response = await getDashboard();
      return response.data;
    },
  });

  if (isLoading) {
    return <h2>Loading Dashboard...</h2>;
  }

  if (isError) {
    return <h2>Failed to load dashboard.</h2>;
  }

  return (
    <div>
      <h1>Enterprise Dashboard</h1>

      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
