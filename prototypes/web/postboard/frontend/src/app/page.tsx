import Feed from "./components/feed";
import SubmissionForm from "./components/form";

export default function Home() {
  let data = [
    { author: "bob", content: "hello" },
    { author: "tim", content: "world" },
  ]

  return (
    <>
      <SubmissionForm />
      <Feed data={data} />
    </>
  )
}
