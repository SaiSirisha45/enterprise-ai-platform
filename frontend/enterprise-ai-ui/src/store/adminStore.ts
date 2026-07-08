import { create } from "zustand";
import type { User } from "../types/admin";

interface AdminState {
  users: User[];
}

export const useAdminStore = create<AdminState>(() => ({
  users: [
    {
      id: 1,
      name: "John Doe",
      email: "john@example.com",
      role: "Admin",
    },
    {
      id: 2,
      name: "Jane Smith",
      email: "jane@example.com",
      role: "User",
    },
  ],
})); 