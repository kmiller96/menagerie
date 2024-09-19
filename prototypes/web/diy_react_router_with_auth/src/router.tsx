import { createBrowserRouter } from "react-router-dom";

import { HomePage } from "./pages/Home";
import { ProtectedPage } from "./pages/Protected";
import { LoginPage } from "./pages/Login";
import { LogoutPage } from "./pages/Logout";

export const router = createBrowserRouter([
  { path: "/", element: <HomePage /> },
  { path: "/protected", element: <ProtectedPage /> },
  { path: "/login", element: <LoginPage /> },
  { path: "/logout", element: <LogoutPage /> },
]);
