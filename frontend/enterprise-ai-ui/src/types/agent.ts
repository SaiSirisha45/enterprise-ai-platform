export interface Agent {
  id: number;
  name: string;
  status: "Running" | "Stopped";
  health: "Healthy" | "Warning" | "Critical";
} 