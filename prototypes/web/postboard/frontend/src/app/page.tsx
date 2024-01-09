import Feed from "./components/feed";

export default function Home() {
  let data = [
    { author: "bob", content: "hello" },
    { author: "tim", content: "world" },
  ]

  return (
    <>
      <Feed data={data} />
    </>
  )
}
