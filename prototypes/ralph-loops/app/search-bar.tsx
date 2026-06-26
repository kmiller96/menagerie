"use client";

import { useRouter, useSearchParams } from "next/navigation";

export function SearchBar({ initialValue }: { initialValue: string }) {
  const router = useRouter();
  const searchParams = useSearchParams();

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const value = e.target.value;
    const params = new URLSearchParams(searchParams.toString());
    if (value) {
      params.set("q", value);
    } else {
      params.delete("q");
    }
    router.push(`?${params.toString()}`);
  }

  return (
    <input
      type="search"
      placeholder="Search notes..."
      defaultValue={initialValue}
      onChange={handleChange}
      className="w-full border rounded p-2"
    />
  );
}
