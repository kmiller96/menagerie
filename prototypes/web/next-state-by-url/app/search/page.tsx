import { NavBar } from "@/components/nav";

export default async function SearchResults({
  searchParams,
}: {
  searchParams: Promise<{ query: string }>;
}) {
  const { query } = await searchParams;
  return (
    <>
      <h1>Search Results</h1>
      <p>Results for "{query}"</p>
    </>
  );
}
