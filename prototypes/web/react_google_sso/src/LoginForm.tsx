import { useGoogleLogin } from "@react-oauth/google";

import { StyledButton } from "./StyledButton";
import { useState } from "react";

export function LoginForm() {
  const [user, setUser] = useState<null | string>(null);

  const login = useGoogleLogin({
    onSuccess: async (tokenResponse) => {
      // -- Get user info -- //
      const response = await fetch(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        { headers: { Authorization: `Bearer ${tokenResponse.access_token}` } }
      );

      const info = await response.json();

      // -- Log to the console -- //
      console.log({
        token: tokenResponse,
        info: info,
      });

      // -- Set user state -- //
      setUser(info.name);
    },
    onError: (errorResponse) => console.log(errorResponse),
  });

  const logout = () => alert("Logout");

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
          padding: 20,
          borderRadius: 10,
          minWidth: 200,
          backgroundColor: "white",
        }}
      >
        <StyledButton onClick={() => login()}>Login</StyledButton>
        <StyledButton onClick={() => logout()}>Logout</StyledButton>
        {user && <p>Welcome, {user}</p>}
      </div>
    </div>
  );
}
