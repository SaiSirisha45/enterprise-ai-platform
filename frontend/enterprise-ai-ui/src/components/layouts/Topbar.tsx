import { Menu } from "lucide-react";
import { useSidebarStore } from "../../store/sidebarStore";
import GlobalSearch from "../search/GlobalSearch";
import NotificationPanel from "../notifications/NotificationPanel";

export default function Topbar() {
  const { toggle } = useSidebarStore();

  return (
    <header className="h-16 border-b bg-white dark:bg-gray-900 dark:text-white flex items-center justify-between px-6"role = "banner">
      
      <div className="flex items-center gap-4">
        <button
          onClick={toggle}
          className="md:hidden p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-800
                      focus:outline-none focus:ring-2 focus:ring-blue-500"
          aria-label="Toggle Sidebar"
        >
          <Menu size={24} />
        </button>

        <h2 className="text-xl font-semibold">
          Enterprise AI Workspace
        </h2>
      </div>

      <div className="flex items-center gap-4">
        <GlobalSearch />
        <NotificationPanel />
      </div>
    </header>
  );
}