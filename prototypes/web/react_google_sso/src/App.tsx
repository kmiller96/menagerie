export function App() {
  console.log(import.meta.env);

  return (
    <div
      id="container"
      style={{
        height: "100vh",
        width: "100vw",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "lightblue",
      }}
    >
      <div
        id="login-container"
        style={{
          display: "flex",
          flexDirection: "column",
          padding: 10,
          backgroundColor: "white",
        }}
      >
        <StyledButton onClick={() => alert("Login")}>Login</StyledButton>
        <StyledButton onClick={() => alert("Logout")}>Logout</StyledButton>
      </div>
    </div>
  );
}

function StyledButton(props: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      style={{
        fontSize: 18,
        marginTop: 5,
        marginBottom: 5,
        paddingLeft: 15,
        paddingRight: 15,
        borderRadius: "8px",
        backgroundColor: "white",
        boxShadow: "3px 3px rgba(0,0,0,0.2)",
        ...props,
      }}
      {...props}
    />
  );
}
