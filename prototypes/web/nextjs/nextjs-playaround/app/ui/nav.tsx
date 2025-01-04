import Link from "next/link";

export function Nav() {
  return (
    <nav style={{ display: "flex", justifyContent: "center", gap: 30 }}>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/posts">Posts</Link>
    </nav>
  );
}
