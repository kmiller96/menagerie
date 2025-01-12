import type { Metadata } from "next";
import "./globals.css";

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
      <body className={`antialiased`}>{children}</body>
    </html>
  );
}
