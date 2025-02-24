import type { Metadata } from "next";
import { Karla } from "next/font/google";

import "./globals.css";

export const karla = Karla({});

export const metadata: Metadata = {
  title: "Landing Page",
  description: "Example landing page",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${karla.className} antialiased min-h-screen`}
        data-theme="black"
      >
        {children}
      </body>
    </html>
  );
}
