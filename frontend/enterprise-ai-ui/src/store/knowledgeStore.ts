import { create } from "zustand";
import type { Document } from "../types/knowledge";

interface KnowledgeState {
  documents: Document[];
  addDocument: (document: Document) => void;
  deleteDocument: (id: number) => void;
}

export const useKnowledgeStore = create<KnowledgeState>((set) => ({
  documents: [],

  addDocument: (document) =>
    set((state) => ({
      documents: [...state.documents, document],
    })),

  deleteDocument: (id) =>
    set((state) => ({
      documents: state.documents.filter((doc) => doc.id !== id),
    })),
})); 