import { useState } from "react";

const notifications = [
  {
    id: 1,
    title: "Workflow Completed",
    message: "Daily report workflow finished successfully.",
  },
  {
    id: 2,
    title: "New AI Agent",
    message: "Knowledge Agent is now available.",
  },
  {
    id: 3,
    title: "System Update",
    message: "Enterprise AI Platform updated successfully.",
  },
];

export default function NotificationPanel() {
  const [open, setOpen] = useState(false);

  return (
    <div className="relative">
      <button
        onClick={() => setOpen(!open)}
        aria-label="Notifications"
        className="rounded-md p-2 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        🔔
      </button>

      {open && (
        <div
          role="dialog"
          aria-label="Notifications"
          className="absolute right-0 mt-2 w-80 rounded-lg border bg-white shadow-lg dark:border-gray-700 dark:bg-gray-800 dark:text-white"
        >
          <h3 className="border-b p-3 font-semibold">
            Notifications
          </h3>

          {notifications.map((item) => (
            <div
              key={item.id}
              className="border-b p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              <p className="font-semibold">{item.title}</p>
              <p className="text-sm">{item.message}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
} 