export default function App() {
  const sidebar = <p>Sidebar</p>;
  const main = <p>Main</p>;

  return (
    <div style={{ display: "flex", flexDirection: "row", height: "100vh" }}>
      <div style={{ backgroundColor: "crimson" }}>{sidebar}</div>
      <div style={{ flexGrow: 1, backgroundColor: "lightblue" }}>{main}</div>
    </div>
  );
}
