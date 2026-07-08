export default function ProfileMenu() {
  return (
    <div
      style={{
        position: "absolute",
        top: 70,
        right: 20,
        width: 200,
        background: "#fff",
        border: "1px solid #ddd",
        borderRadius: 8,
        padding: 15,
        boxShadow: "0 2px 10px rgba(0,0,0,0.15)",
        zIndex: 1000,
      }}
    >
      <h3>Profile</h3>

      <p>My Account</p>

      <p>Settings</p>

      <p>Logout</p>
    </div>
  );
} 