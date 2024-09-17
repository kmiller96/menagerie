import { useState } from "react";

import { useAuth } from "@/hooks/useAuth";

import { BasePage } from "./Base";

const USERNAME = "admin";
const PASSWORD = "admin";

export function LoginPage() {
  return (
    <BasePage>
      <h1>Login Page</h1>
      <LoginForm />
    </BasePage>
  );
}

function LoginForm() {
  // -- State & Hooks -- //
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const { login } = useAuth();

  // -- Handlers -- //
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (username === USERNAME && password === PASSWORD) {
      await login(username);
      console.log("Login success!");
    } else {
      alert("Login failed");
    }
  };

  // -- Render -- //
  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="username">Username</label>
        <input
          id="username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
  );
}
