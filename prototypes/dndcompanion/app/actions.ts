"use server";

import { createArticle } from "@/lib/handlers";
import { redirect } from "next/navigation";

export async function submitCreateArticle(formData: FormData): Promise<void> {
  const title = formData.get("title")!.toString();
  const content = formData.get("content")!.toString();

  const article = await createArticle({ title, content });

  redirect(`/articles/${article.id}`);
}
