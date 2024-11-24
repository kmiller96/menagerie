import { Navigator } from "./Navigator";
import { Editor } from "./Editor";

export default function App() {
  return (
    <div style={{ display: "flex", flexDirection: "row", height: "100vh" }}>
      <div style={{ backgroundColor: "crimson", width: "20vw" }}>
        <Navigator />
      </div>
      <div style={{ flexGrow: 1, backgroundColor: "lightblue" }}>
        <Editor />
      </div>
    </div>
  );
}
