const ResetPassword = () => {
  return (
    <div
      style={{
        maxWidth: "400px",
        margin: "60px auto",
      }}
    >
      <h1>Reset Password</h1>

      <input
        type="password"
        placeholder="New Password"
        style={{
          width: "100%",
          padding: "10px",
          marginBottom: "15px",
        }}
      />

      <input
        type="password"
        placeholder="Confirm Password"
        style={{
          width: "100%",
          padding: "10px",
          marginBottom: "20px",
        }}
      />

      <button
        style={{
          width: "100%",
          padding: "10px",
        }}
      >
        Reset Password
      </button>
    </div>
  );
};

export default ResetPassword; 