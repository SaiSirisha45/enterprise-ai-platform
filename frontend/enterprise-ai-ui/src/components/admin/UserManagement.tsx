import { useAdminStore } from "../../store/adminStore";

const UserManagement = () => {
  const users = useAdminStore((state) => state.users);

  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "20px",
        borderRadius: "8px",
        marginBottom: "20px",
      }}
    >
      <h2>User Management</h2>

      {users.map((user) => (
        <div key={user.id} style={{ marginBottom: "10px" }}>
          <strong>{user.name}</strong>
          <br />
          {user.email}
          <br />
          Role: {user.role}
        </div>
      ))}
    </div>
  );
};

export default UserManagement; 