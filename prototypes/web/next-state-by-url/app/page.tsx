function Title() {
  return (
    <div className="mb-5">
      <h1 className="text-5xl">Product Search</h1>
      <h2 className="italic">What product would you like to access?</h2>
    </div>
  );
}

function SearchForm() {
  return (
    <div className="pb-[200px] w-full">
      <form action="/search" method="GET">
        <div className="flex flex-row join">
          <input
            type="text"
            name="query"
            placeholder="What are you looking for?"
            className="input input-bordered flex-grow join-item"
          />
          <button className="btn btn-primary join-item" type="submit">
            Search
          </button>
        </div>
      </form>
    </div>
  );
}

export default function Home() {
  return (
    <div className="flex flex-col flex-grow items-center justify-center h-min-screen">
      <div className="w-6/12 flex flex-col items-center justify-center">
        <Title />
        <SearchForm />
      </div>
    </div>
  );
}
