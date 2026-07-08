import DashboardLayout from "../../layouts/DashboardLayout";
import WorkflowEditor from "../../components/workflows/WorkflowEditor";
import WorkflowList from "../../components/workflows/WorkflowList";
import WorkflowHistory from "../../components/workflows/WorkflowHistory";

const Workflows = () => {
  return (
    <DashboardLayout>
      <h1>Workflow Builder</h1>

      <WorkflowEditor />

      <WorkflowList />

      <WorkflowHistory />
    </DashboardLayout>
  );
};

export default Workflows; 