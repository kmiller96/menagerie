import { NavBar } from "@/components/NavBar";

export function LogoutPage() {
  return (
    <>
      <NavBar />
      <h1>Logout</h1>
      <form
        onSubmit={() => {
          localStorage.removeItem("token");
        }}
      >
        <button type="submit">Logout</button>
      </form>
    </>
  );
}
