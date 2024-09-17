import { createContext, useContext, useMemo } from "react";

import { useNavigate } from "react-router-dom";
import { useLocalStorage } from "./useLocalStorage";

// ----------- //
// -- Types -- //
// ----------- //

type AuthContextValue = {
  user: string | null;
  login: (user: string) => Promise<void>;
  logout: () => void;
};

// -------------------- //
// -- Context Object -- //
// -------------------- //

const AuthContext = createContext<AuthContextValue>({
  user: null,
  // @ts-ignore: 6133
  login: (user: string) => {},
  logout: () => {},
});

// -------------- //
// -- Provider -- //
// -------------- //

export function AuthProvider({ children }: { children: React.ReactNode }) {
  // -- State & Hooks -- //
  const [user, setUser] = useLocalStorage("user", null);
  const navigate = useNavigate();

  // -- Handlers -- //
  // TODO: Replace any with the actual type
  const login = async (user: any) => {
    setUser(user);
    navigate("/", { replace: true });
  };

  const logout = () => {
    setUser(null);
    navigate("/", { replace: true });
  };

  // -- Return Provider -- //
  const value = useMemo(
    () => ({
      user,
      login,
      logout,
    }),
    [user]
  );

  return <AuthContext.Provider value={value} children={children} />;
}

// ---------- //
// -- Hook -- //
// ---------- //

export function useAuth() {
  return useContext(AuthContext);
}
