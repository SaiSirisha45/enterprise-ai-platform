import { Outlet } from "react-router-dom";
import Sidebar from "../components/layouts/Sidebar";
import Topbar from "../components/layouts/Topbar";
import { useSidebarStore } from "../store/sidebarStore";

export default function AppLayout() {
  const { isOpen, close } = useSidebarStore();

  return (
    <div className="flex min-h-screen bg-gray-100 dark:bg-gray-900">
      <Sidebar />

      {isOpen && (
        <div
          className="fixed inset-0 z-40 bg-black/40 md:hidden"
          onClick={close}
        />
      )}

      <div className="flex flex-1 flex-col">
        <Topbar />

        <main
          role="main"
          className="flex-1 overflow-auto p-6"
        >
          <Outlet />
        </main>
      </div>
    </div>
  );
} 