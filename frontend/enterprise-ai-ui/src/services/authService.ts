import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

// Register
export const registerUser = async (data: {
  name: string;
  email: string;
  password: string;
}) => {
  const response = await API.post("/auth/register", data);
  return response.data;
};

// Login
export const loginUser = async (data: {
  email: string;
  password: string;
}) => {
  const response = await API.post("/auth/login", data);

  if (response.data.access_token) {
    localStorage.setItem("token", response.data.access_token);
  }

  return response.data;
};

// Logout
export const logoutUser = () => {
  localStorage.removeItem("token");
};

// Get Token
export const getToken = () => {
  return localStorage.getItem("token");
};

// Authenticated API
export const authAPI = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

authAPI.interceptors.request.use((config) => {
  const token = getToken();

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

export default API; 