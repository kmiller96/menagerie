import data from "@/app/data";

import { Center } from "@/components/layout";

function Title({ query }: { query: string }) {
  return (
    <div className="mb-5">
      <h1 className="text-5xl">Search Results</h1>
      <h2 className="italic">Results for "{query}"</h2>
    </div>
  );
}

function Results({ results }: { results: typeof data }) {
  return (
    <div className="w-full">
      <table className="table table-zebra">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {results.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.title}</td>
              <td>{item.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default async function SearchResults({
  searchParams,
}: {
  searchParams: Promise<{ query: string }>;
}) {
  const { query } = await searchParams;

  const results = data.filter((item) =>
    item.title.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <Center>
      <div className="flex flex-col flex-grow justify-center items-start w-8/12">
        <Title query={query} />
        <Results results={results} />
      </div>
    </Center>
  );
}
