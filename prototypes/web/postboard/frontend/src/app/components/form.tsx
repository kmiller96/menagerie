"use client";

import React, { useState } from "react";
import styles from "./form.module.css";

/** Defines the submission form */
export default function SubmissionForm() {
  const [content, setContent] = useState("");
  const [author, setAuthor] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    fetch("/api/post", {
      method: "POST",
      body: JSON.stringify({ author, content }),
    })
      .then((response) => response.json())
      .then((response) => console.log(JSON.stringify(response)));
  };

  return (
    <div className={styles.form}>
      <form onSubmit={handleSubmit}>
        <div>
          <textarea
            id="content"
            autoCorrect="on"
            placeholder="What would you like to say?"
            required
            onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => {
              setContent(e.target.value);
            }}
          />
        </div>
        <div>
          <input
            type="text"
            id="author"
            placeholder="Name (Optional)"
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
              setAuthor(e.target.value);
            }}
          />
        </div>
        <div>
          <input type="submit" id="submit" />
        </div>
      </form>
    </div>
  );
}
