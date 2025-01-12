import { ThemeToggle } from "@/components/themeToggle";

export default function Home() {
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="flex flex-col w-6/12 justify-center align-middle">
        <ThemeToggle />
        <button className="btn btn-primary">One</button>
        <button className="btn btn-secondary">Two</button>
        <button className="btn btn-accent btn-outline">Three</button>
      </div>
    </div>
  );
}
