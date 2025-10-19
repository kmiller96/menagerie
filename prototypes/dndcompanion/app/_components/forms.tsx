"use client";

import { submitCreateArticle } from "../actions";
import React from "react";

export function CreateArticleForm() {
  // Handlers
  const handleKeyDown = (event: React.KeyboardEvent<HTMLFormElement>) => {
    if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
      event.currentTarget.requestSubmit();
    }
  };

  // Render
  return (
    <form
      action={submitCreateArticle}
      onKeyDown={handleKeyDown}
      className="flex flex-col gap-2"
    >
      <input
        type="text"
        name="title"
        placeholder="Title"
        className="input w-full"
      />
      <textarea
        name="content"
        placeholder="Content"
        rows={20}
        className="textarea w-full"
      />
      <input type="submit" value="Create Article" className="btn btn-primary" />
    </form>
  );
}
