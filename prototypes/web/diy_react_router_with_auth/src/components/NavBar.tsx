import { Link } from "react-router-dom";

export function NavBar() {
  return (
    <nav>
      <ul
        style={{
          display: "flex",
          gap: "1rem",

          margin: 0,
          padding: 0,

          width: "100%",
          backgroundColor: "lightgray",

          textDecoration: "none",
          listStyleType: "none",
        }}
      >
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/protected">Protected</Link>
        </li>
        <li>
          <Link to="/login">Login</Link>
        </li>
        <li>
          <Link to="/logout">Logout</Link>
        </li>
      </ul>
    </nav>
  );
}
