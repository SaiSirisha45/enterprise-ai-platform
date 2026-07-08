import { useAgentStore } from "../../store/agentStore";

interface Props {
  id: number;
}

const AgentControls = ({ id }: Props) => {
  const startAgent = useAgentStore((state) => state.startAgent);
  const stopAgent = useAgentStore((state) => state.stopAgent);
  const restartAgent = useAgentStore((state) => state.restartAgent);

  return (
    <div style={{ marginTop: "10px" }}>
      <button onClick={() => startAgent(id)}>Start</button>

      <button
        onClick={() => stopAgent(id)}
        style={{ marginLeft: "10px" }}
      >
        Stop
      </button>

      <button
        onClick={() => restartAgent(id)}
        style={{ marginLeft: "10px" }}
      >
        Restart
      </button>
    </div>
  );
};

export default AgentControls; 