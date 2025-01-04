import { Nav } from "@/app/ui/nav";

export default async function Posts() {
  const data = await fetch("https://api.vercel.app/blog");
  const posts = await data.json();

  return (
    <>
      <Nav />
      <h1 style={{ marginBottom: 20 }}>Posts Page</h1>
      {posts.map((post: { id: string; title: string; body: string }) => (
        <div
          key={post.id}
          style={{ margin: 10, border: "1px solid #ccc", padding: 10 }}
        >
          <h3>{post.title}</h3>
          <p>{post.body}</p>
        </div>
      ))}
    </>
  );
}
