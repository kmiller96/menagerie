import { getAllTags } from "@/lib/tags";
import { getNotes } from "@/lib/queries";
import { ComposeForm } from "./compose-form";
import { SearchBar } from "./search-bar";
import { TagPills } from "./tag-pills";
import { NoteList } from "./note-list";

interface Props {
  searchParams: Promise<{ q?: string; tags?: string }>;
}

export default async function Home({ searchParams }: Props) {
  const { q, tags } = await searchParams;
  const searchQuery = q ?? "";
  const selectedTagIds = tags
    ? tags.split(",").map(Number).filter((n) => !isNaN(n))
    : [];

  const notes = getNotes({ searchQuery, selectedTagIds });
  const allTags = getAllTags();

  return (
    <div className="max-w-2xl mx-auto px-4 py-6 sm:px-6 sm:py-8 space-y-6">
      <h1 className="text-2xl sm:text-3xl font-bold tracking-tight">Notes</h1>
      <ComposeForm />
      <SearchBar initialValue={searchQuery} />
      <TagPills tags={allTags} selectedIds={selectedTagIds} />
      <NoteList
        notes={notes}
        allTags={allTags}
        hasActiveFilters={!!(searchQuery || selectedTagIds.length > 0)}
      />
    </div>
  );
}
