import { File } from "lucide-react";

import { Article } from "@/lib/types";
import Link from "next/link";

// ------------------------ //
// -- Application Navbar -- //
// ------------------------ //

export function Navbar() {
  return (
    <nav className="navbar bg-neutral text-neutral-content shadow-sm flex flex-row items-center justify-between p-2">
      <Link href="/">Home</Link>
      <Link href="/articles/new">New Article</Link>
    </nav>
  );
}

// --------------------- //
// -- Article Sidebar -- //
// --------------------- //

function ArticleSidebarRow({ article }: Readonly<{ article: Article }>) {
  return (
    <div className="p-1">
      <Link href={`/articles/${article.id}`} className="flex flex-row gap-1">
        <File />
        {article.title}
      </Link>
    </div>
  );
}

/** Displays a list of articles in the sidebar. */
// TODO: Use something like this: https://daisyui.com/components/drawer/#responsive
export function ArticleSidebar({
  articles,
}: Readonly<{ articles: Article[] }>) {
  return (
    <div className="h-screen border-r-2 space-y-1 p-1">
      {articles.map((article) => (
        <ArticleSidebarRow key={article.id} article={article} />
      ))}
    </div>
  );
}
