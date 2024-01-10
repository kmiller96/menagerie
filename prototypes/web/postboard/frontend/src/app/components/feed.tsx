"use client";

import { useEffect, useState } from "react";

import styles from "./feed.module.css";

type FeedData = Array<{ author: string; content: string }>;

/** A feed of posts by users.  */
export default function Feed() {
  const [posts, setPosts] = useState<FeedData>([]);

  useEffect(() => {
    setInterval(() => {
      setPosts([
        { author: "bob", content: "hello" },
        { author: "tim", content: "world" },
        { author: "paul", content: "goodbye!" },
      ]); // TODO: Temporary testing code
    }, 1000 * 5);
  }, []);

  return (
    <div className={styles.feed}>
      {posts.map((post, i) => (
        <FeedPost key={i} author={post.author} content={post.content} />
      ))}
    </div>
  );
}

/** Individual feed post */
function FeedPost({ author, content }: { author: string; content: string }) {
  return (
    <div className={styles.post}>
      <h1>@{author}</h1>
      <p>{content}</p>
    </div>
  );
}
