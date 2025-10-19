import sql from "./database";
import { Article } from "./types";

export async function listArticles(): Promise<Article[]> {
  return await sql`SELECT * FROM articles ORDER BY title ASC`;
}

export async function getArticle(id: string): Promise<Article> {
  const data =
    (await sql`SELECT * FROM articles WHERE id = ${id}`) as Article[];

  if (data.length === 0) {
    throw new Error("Article not found");
  }

  return data[0];
}

export async function createArticle(article: {
  title: string;
  content: string;
}): Promise<Article> {
  const data: Article[] = await sql`
    INSERT INTO articles (title, content) 
    VALUES (${article.title}, ${article.content})
    RETURNING *
  `;

  return data[0];
}
