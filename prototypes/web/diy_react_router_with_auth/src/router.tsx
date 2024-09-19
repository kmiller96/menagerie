import { createBrowserRouter } from "react-router-dom";

import { HomePage } from "./pages/Home";
import { LoginPage } from "./pages/Login";
import { ProtectedPage } from "./pages/Protected";

export const router = createBrowserRouter([
  { path: "/", element: <HomePage /> },
  { path: "/login", element: <LoginPage /> },
  { path: "/protected", element: <ProtectedPage /> },
]);
