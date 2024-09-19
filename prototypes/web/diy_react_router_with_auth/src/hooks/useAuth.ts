import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export function useAuth({
  redirectOnFail = true,
}: {
  redirectOnFail?: boolean;
}) {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token && redirectOnFail) {
      navigate("/login");
    }
  }, [token]);

  return token;
}
