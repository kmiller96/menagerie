import type { Metadata } from "next";
import "./globals.css";

import { Navbar } from "@/app/_components/nav";

export const metadata: Metadata = {
  title: "⚔️ D&D Companion",
  description: "A companion app for Dungeons & Dragons.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`antialiased`}>
        <Navbar />
        {children}
      </body>
    </html>
  );
}
