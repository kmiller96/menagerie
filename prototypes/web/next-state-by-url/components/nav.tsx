"use client";

import { useRouter, usePathname } from "next/navigation";

export function NavBar() {
  const router = useRouter();
  const pathname = usePathname();

  return (
    <nav className="navbar">
      <div className="gap-2">
        <button
          className={pathname === "/" ? "hidden" : "text-xl"}
          onClick={() => router.back()}
        >
          <svg
            className="lucide lucide-arrow-left"
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="m12 19-7-7 7-7" />
            <path d="M19 12H5" />
          </svg>
        </button>
        <button className="text-xl">State by URL</button>
      </div>
      <div className="flex-grow justify-end">
        <ul>
          <li>
            <a href="/">Home</a>
          </li>
        </ul>
      </div>
    </nav>
  );
}
