import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";

import AppLayout from "../layouts/AppLayout";
import ProtectedRoute from "./ProtectedRoute";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>

        {/* PUBLIC ROUTE */}
        <Route path="/login" element={<Login />} />

        {/* PROTECTED ENTERPRISE LAYOUT */}
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <AppLayout />
            </ProtectedRoute>
          }
        >

          {/* NESTED ROUTES INSIDE LAYOUT */}
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="chat" element={<div>Chat Page</div>} />
          <Route path="knowledge" element={<div>Knowledge Base</div>} />
          <Route path="workflows" element={<div>Workflows</div>} />
          <Route path="agents" element={<div>Agents</div>} />
          <Route path="analytics" element={<div>Analytics</div>} />
          <Route path="admin" element={<div>Admin</div>} />
          <Route path="settings" element={<div>Settings</div>} />

        </Route>

      </Routes>
    </BrowserRouter>
  );
}