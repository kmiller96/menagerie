"use client";

import { useEffect, useState } from "react";
import Feed from "./components/feed";
import SubmissionForm from "./components/form";

import { FeedData } from "./types";
import { fetchPostsData } from "./handlers";

const POLL_SECONDS = 5;

export default function Home() {
  // State
  const [posts, setPosts] = useState<FeedData>([]);

  // Functions
  const updatePostsData = () => {
    fetchPostsData().then((data) => setPosts(data));
  };

  // Effects
  useEffect(() => {
    updatePostsData();
    setInterval(updatePostsData, 1000 * POLL_SECONDS);
  }, []);

  return (
    <>
      <SubmissionForm postSubmit={() => updatePostsData()} />
      <Feed posts={posts} />
    </>
  );
}
