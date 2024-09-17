import { Routes, Route } from "react-router-dom";

import { ProtectedRoute } from "@/components/ProtectedRoute";

import { HomePage } from "./pages/Home";
import { PublicPage } from "./pages/Public";
import { PrivatePage } from "./pages/Private";
import { LoginPage } from "./pages/Login";

export function Router() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/public" element={<PublicPage />} />
      <Route
        path="/private"
        element={
          <ProtectedRoute>
            <PrivatePage />
          </ProtectedRoute>
        }
      />
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  );
}
