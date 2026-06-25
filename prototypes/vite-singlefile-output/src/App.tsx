import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen gap-2">
      <h1 className="text-2xl mb-2">Single Page Demo</h1>
      <aside className="text-sm text-gray-500 border bg-amber-50 p-2 rounded-md w-fit mb-2">
        This is a demo showing how you can make a single page output with Vite.
      </aside>
      <div className="flex gap-2 items-center">
        <button onClick={() => setCount((count) => count + 1)}>+</button>
        <span>{count}</span>
        <button onClick={() => setCount((count) => count - 1)}>-</button>
      </div>
    </div>
  );
}

export default App;
