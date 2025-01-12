import { ThemeToggle } from "@/components/themeToggle";

export default function Home() {
  return (
    <div>
      <ThemeToggle />
      <button className="btn btn-primary">One</button>
      <button className="btn btn-secondary">Two</button>
      <button className="btn btn-accent btn-outline">Three</button>
    </div>
  );
}
