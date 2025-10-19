import { listArticles } from "@/lib/handlers";
import { ArticleSidebar } from "@/app/_components/nav";

export default async function ArticlesLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  const articles = await listArticles();

  return (
    <div className="flex flex-row">
      <ArticleSidebar articles={articles} />
      <div className="flex-grow h-screen overflow-y-scroll p-2">{children}</div>
    </div>
  );
}
