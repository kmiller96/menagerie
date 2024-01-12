"use client";

import styles from "./feed.module.css";
import { FeedData } from "../types";

/** A feed of posts by users.  */
export default function Feed({ posts }: { posts: FeedData }) {
  return (
    <div className={styles.feed}>
      {posts.map((post, i) => (
        <FeedPost
          key={i}
          created={post.created}
          author={post.author}
          content={post.content}
        />
      ))}
    </div>
  );
}

/** Individual feed post */
function FeedPost({
  author,
  content,
  created,
}: {
  author: string;
  content: string;
  created: string;
}) {
  return (
    <div className={styles.post}>
      <h1>@{author}</h1>
      <h2>{created}</h2>
      <p>{content}</p>
    </div>
  );
}
