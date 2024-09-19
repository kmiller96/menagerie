import { NavBar } from "@/components/NavBar";

export function LoginPage() {
  return (
    <>
      <NavBar />
      <h1>Login</h1>
      <form>
        <label>
          Username:
          <input type="text" />
        </label>
        <br />
        <label>
          Password:
          <input type="password" />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </>
  );
}
