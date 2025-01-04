import { Nav } from "../ui/nav";

export default async function AboutPage() {
  return (
    <>
      <Nav />
      <h1 style={{ marginBottom: 20 }}>About Page</h1>
      <p>
        This is the about page. It is a static page that is not fetched from an
        API.
      </p>
    </>
  );
}
