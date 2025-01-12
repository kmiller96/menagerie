"use client";

import { useRouter } from "next/navigation";

export function NavBar() {
  const router = useRouter();
  return (
    <nav>
      <ul>
        <li>
          <a
            style={{ cursor: "pointer" }}
            onClick={() => {
              router.back();
            }}
          >
            Go Back
          </a>
        </li>
      </ul>
    </nav>
  );
}
