import { useAuth } from "@/hooks/useAuth";
import { NavBar } from "@/components/NavBar";

export function HomePage() {
  const token = useAuth({ redirectOnFail: false });

  return (
    <>
      <NavBar />
      <h1>Home</h1>
      <p>Welcome to the home page!</p>
      <p>{token ? "You are logged in!" : "You are not logged in!"}</p>
    </>
  );
}
