"use client";

import { useEffect, useState } from "react";

import styles from "./feed.module.css";

const POLL_SECONDS = 5;

/** Type information */
type FeedData = Array<{ author: string; content: string; created: string }>;

/** A feed of posts by users.  */
export default function Feed() {
  const [posts, setPosts] = useState<FeedData>([]);

  const updatePostsData = () => {
    fetch("/api/feed")
      .then((res) => res.json())
      .then((data: FeedData) => {
        data.map((obj) => {
          const dt = new Date(Date.parse(obj.created));

          const year = dt.getFullYear();
          const month = new String(dt.getMonth() + 1).padStart(2, "0");
          const day = new String(dt.getDate()).padStart(2, "0");
          const hour = new String(dt.getHours()).padStart(2, "0");
          const minute = new String(dt.getMinutes()).padStart(2, "0");

          obj.created = `${year}-${month}-${day} ${hour}:${minute}`;
        });

        return data;
      })
      .then((res) => setPosts(res));
  };

  useEffect(() => {
    updatePostsData();
    setInterval(updatePostsData, 1000 * POLL_SECONDS);
  }, []);

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
