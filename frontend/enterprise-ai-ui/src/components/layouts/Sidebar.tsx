import { NavLink } from "react-router-dom";
import { useSidebarStore } from "../../store/sidebarStore";

export default function Sidebar() {
  const { isOpen, close } = useSidebarStore();

  const menu = [
    { name: "Dashboard", path: "/dashboard" },
    { name: "AI Chat", path: "/chat" },
    { name: "Knowledge Base", path: "/knowledge" },
    { name: "Agents", path: "/agents" },
    { name: "Workflows", path: "/workflows" },
    { name: "Analytics", path: "/analytics" },
    { name: "Admin", path: "/admin" },
    { name: "Settings", path: "/settings" },
    { name: "Profile", path: "/profile" },
  ];

  return (
    <aside
      className={`
        fixed md:static
        top-0 left-0
        h-screen
        w-64
        bg-gray-900
        text-white
        transform
        transition-transform
        duration-300
        z-50
        ${isOpen ? "translate-x-0" : "-translate-x-full"}
        md:translate-x-0
      `}
    >
      <h2 className="text-2xl font-bold p-5 border-b border-gray-700">
        Enterprise AI
      </h2>

      <nav className="mt-4">
        {menu.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            onClick={close}
            className={({ isActive }) =>
              `block px-5 py-3 hover:bg-gray-700 ${
                isActive ? "bg-gray-700" : ""
              }`
            }
          >
            {item.name}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
} 