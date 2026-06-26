"use client";

import { useRouter, useSearchParams } from "next/navigation";

export function TagPills({
  tags,
  selectedIds,
}: {
  tags: { id: number; name: string }[];
  selectedIds: number[];
}) {
  const router = useRouter();
  const searchParams = useSearchParams();

  function toggleTag(id: number) {
    const params = new URLSearchParams(searchParams.toString());
    const selected = selectedIds.includes(id)
      ? selectedIds.filter((tid) => tid !== id)
      : [...selectedIds, id];
    if (selected.length > 0) {
      params.set("tags", selected.join(","));
    } else {
      params.delete("tags");
    }
    router.push(`?${params.toString()}`);
  }

  return (
    <div className="flex gap-2 flex-wrap">
      {tags.map((tag) => (
        <button
          key={tag.id}
          onClick={() => toggleTag(tag.id)}
          className={`px-3 py-1 rounded-full text-sm border cursor-pointer ${
            selectedIds.includes(tag.id)
              ? "bg-blue-500 text-white border-blue-500"
              : "bg-white text-gray-700 border-gray-300"
          }`}
        >
          #{tag.name}
        </button>
      ))}
    </div>
  );
}
