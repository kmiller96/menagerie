import type { Metadata } from "next";
import { initSchema } from "@/lib/schema";
import "./globals.css";

initSchema();

export const metadata: Metadata = {
  title: "Notes",
  description: "A simple note-taking app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-900 min-h-screen antialiased">{children}</body>
    </html>
  );
}
