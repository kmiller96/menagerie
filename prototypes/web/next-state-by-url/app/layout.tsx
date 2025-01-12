import type { Metadata } from "next";
import "./globals.css";
import { NavBar } from "@/components/nav";

export const metadata: Metadata = {
  title: "State by URL",
  description:
    "Attemping to share application state using URLs, not client state",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body data-theme className={`antialiased flex flex-col min-h-screen`}>
        <NavBar />
        {children}
      </body>
    </html>
  );
}
