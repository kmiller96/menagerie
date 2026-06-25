import { useState } from "react";

function Button({
  onClick,
  children,
}: {
  onClick: () => void;
  children: React.ReactNode;
}) {
  return (
    <button
      className="px-2 py-1 bg-blue-500 text-white rounded"
      onClick={onClick}
    >
      {children}
    </button>
  );
}

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen gap-2">
      <h1 className="text-2xl mb-2">Single Page Demo</h1>
      <aside className="text-sm text-gray-500 border bg-amber-50 p-2 rounded-md w-fit mb-2">
        This is a demo showing how you can make a single page output with Vite.
      </aside>
      <div className="flex gap-2 items-center">
        <Button onClick={() => setCount((count) => count + 1)}>+</Button>
        <span>{count}</span>
        <Button onClick={() => setCount((count) => count - 1)}>-</Button>
      </div>
    </div>
  );
}

export default App;
