import DashboardLayout from "../../layouts/DashboardLayout";
import UserManagement from "../../components/admin/UserManagement";
import RoleManagement from "../../components/admin/RoleManagement";
import SystemSettings from "../../components/admin/SystemSettings";
import AuditLogs from "../../components/admin/AuditLogs";
import ApiKeys from "../../components/admin/ApiKeys";

const Admin = () => {
  return (
    <DashboardLayout>
      <h1>Admin Console</h1>

      <UserManagement />

      <RoleManagement />

      <SystemSettings />

      <AuditLogs />

      <ApiKeys />
    </DashboardLayout>
  );
};

export default Admin; 