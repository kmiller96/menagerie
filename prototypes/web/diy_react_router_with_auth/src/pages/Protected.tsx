import { useAuth } from "@/hooks/useAuth";
import { NavBar } from "@/components/NavBar";

export function ProtectedPage() {
  const token = useAuth({ redirectOnFail: true });

  return (
    <>
      <NavBar />
      <h1>Protected Page</h1>
      <p>You are in a super secret protected page. Welcome!</p>
    </>
  );
}
