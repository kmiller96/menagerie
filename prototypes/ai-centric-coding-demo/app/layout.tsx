import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Link Shortening Service",
  description: "Shortens links and tracks clicks.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
