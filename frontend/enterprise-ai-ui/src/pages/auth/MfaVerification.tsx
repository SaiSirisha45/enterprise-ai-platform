const MfaVerification = () => {
  return (
    <div
      style={{
        maxWidth: "400px",
        margin: "60px auto",
      }}
    >
      <h1>MFA Verification</h1>

      <input
        type="text"
        placeholder="Enter OTP"
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
        Verify
      </button>
    </div>
  );
};

export default MfaVerification; 