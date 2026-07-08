import { useWorkflowStore } from "../../store/workflowStore";

interface Props {
  id: number;
}

const WorkflowControls = ({ id }: Props) => {
  const runWorkflow = useWorkflowStore((state) => state.runWorkflow);
  const pauseWorkflow = useWorkflowStore((state) => state.pauseWorkflow);
  const deleteWorkflow = useWorkflowStore((state) => state.deleteWorkflow);

  return (
    <div style={{ marginTop: "10px" }}>
      <button onClick={() => runWorkflow(id)}>Run</button>

      <button
        onClick={() => pauseWorkflow(id)}
        style={{ marginLeft: "10px" }}
      >
        Pause
      </button>

      <button
        onClick={() => deleteWorkflow(id)}
        style={{ marginLeft: "10px" }}
      >
        Delete
      </button>
    </div>
  );
};

export default WorkflowControls; 