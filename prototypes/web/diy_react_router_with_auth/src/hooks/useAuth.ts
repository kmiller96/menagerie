import { useNavigate } from "react-router-dom";

export function useAuth({
  redirectOnFail = true,
}: {
  redirectOnFail?: boolean;
}) {
  const token = localStorage.getItem("token");

  if (!token && redirectOnFail) {
    const navigate = useNavigate();
    navigate("/login");
    console.log("Redirecting to login page...");
    // TODO: Navigate to login page
  }

  return token;
}
