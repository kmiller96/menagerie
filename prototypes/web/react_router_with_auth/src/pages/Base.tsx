import { Links } from "@/components/Links";

export function BasePage({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <Links />
      {children}
    </div>
  );
}
