import { create } from "zustand";
import type { Workflow } from "../types/workflow";

interface WorkflowState {
  workflows: Workflow[];

  runWorkflow: (id: number) => void;
  pauseWorkflow: (id: number) => void;
  deleteWorkflow: (id: number) => void;
}

export const useWorkflowStore = create<WorkflowState>((set) => ({
  workflows: [
    {
      id: 1,
      name: "Customer Support Workflow",
      status: "Running",
    },
    {
      id: 2,
      name: "Document Processing Workflow",
      status: "Paused",
    },
  ],

  runWorkflow: (id) =>
    set((state) => ({
      workflows: state.workflows.map((workflow) =>
        workflow.id === id
          ? { ...workflow, status: "Running" }
          : workflow
      ),
    })),

  pauseWorkflow: (id) =>
    set((state) => ({
      workflows: state.workflows.map((workflow) =>
        workflow.id === id
          ? { ...workflow, status: "Paused" }
          : workflow
      ),
    })),

  deleteWorkflow: (id) =>
    set((state) => ({
      workflows: state.workflows.filter(
        (workflow) => workflow.id !== id
      ),
    })),
})); 