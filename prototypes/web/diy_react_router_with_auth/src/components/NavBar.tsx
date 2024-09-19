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
          <a href="/">Home</a>
        </li>
        <li>
          <a href="/about">About</a>
        </li>
      </ul>
    </nav>
  );
}
