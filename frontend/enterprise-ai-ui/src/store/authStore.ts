import { create } from "zustand";

type AuthStore = {
  token: string | null;
  login: (token: string) => void;
  logout: () => void;
};

export const useAuthStore = create<AuthStore>((set) => ({
  token: localStorage.getItem("access_token"),

  login: (token) => {
    localStorage.setItem("access_token", token);
    set({ token });
  },

  logout: () => {
    localStorage.removeItem("access_token");
    set({ token: null });
  },
})); 