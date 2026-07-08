import { AxiosError } from "axios";
import toast from "react-hot-toast"; // npm install react-hot-toast

export const handleApiError = (error: unknown) => {
  if (error instanceof AxiosError) {
    const status = error.response?.status;
    const message =
      (error.response?.data as any)?.message || error.message || "Something went wrong";

    switch (status) {
      case 400:
        toast.error(`Bad Request: ${message}`);
        break;
      case 401:
        toast.error("Session expired. Please log in again.");
        break;
      case 403:
        toast.error("You don't have permission to do this.");
        break;
      case 404:
        toast.error("Resource not found.");
        break;
      case 500:
        toast.error("Server error. Please try again later.");
        break;
      default:
        toast.error(message);
    }
  } else {
    toast.error("Unexpected error occurred.");
  }
}; 