import { createBrowserRouter } from "react-router-dom";

import { ProtectedRoute } from "@/components/ProtectedRoute";

import { HomePage } from "./pages/Home";
import { PublicPage } from "./pages/Public";
import { PrivatePage } from "./pages/Private";
import { LoginPage } from "./pages/Login";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "/public",
    element: <PublicPage />,
  },
  {
    path: "/private",
    element: (
      <ProtectedRoute>
        <PrivatePage />
      </ProtectedRoute>
    ),
  },
  {
    path: "/login",
    element: <LoginPage />,
  },
]);
