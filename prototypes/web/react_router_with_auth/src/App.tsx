import { AuthProvider } from "./hooks/useAuth";
import { Router } from "./Router";

export default function App() {
  return (
    <AuthProvider>
      <Router />
    </AuthProvider>
  );
}
