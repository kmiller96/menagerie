import { GoogleOAuthProvider } from "@react-oauth/google";
import { LoginForm } from "./LoginForm";

export function App() {
  return (
    <GoogleOAuthProvider clientId={import.meta.env.VITE_CLIENT_ID}>
      <LoginForm />
    </GoogleOAuthProvider>
  );
}
