import Image from "next/image";

export default function Home() {
  return (
    <>
      <h1>Product Search</h1>
      <p>What product would you like to access?</p>
      <form action="/search" method="GET">
        <input type="text" name="query" />
        <button type="submit">Search</button>
      </form>
    </>
  );
}
