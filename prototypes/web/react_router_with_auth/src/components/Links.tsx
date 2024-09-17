export function Links() {
  return (
    <ul
      style={{
        display: "flex",
        flexDirection: "row",
        textDecoration: "none",
        listStyleType: "none",
        padding: 0,
        margin: 0,
        gap: "1rem",
      }}
    >
      <li>
        <a href="/">Home</a>
      </li>
      <li>
        <a href="/public">Public</a>
      </li>
      <li>
        <a href="/private">Private</a>
      </li>
      <li>
        <a href="/login">Login</a>
      </li>
    </ul>
  );
}
