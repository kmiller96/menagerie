import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "DaisyUI Exploration",
  description: "Exploring DaisyUI with Next.js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body data-theme className={`antialiased`}>
        {children}
      </body>
    </html>
  );
}
