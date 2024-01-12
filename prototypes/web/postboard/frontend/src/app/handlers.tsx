/** Contains handler functions for the frontend. */

import { FeedData } from "./types";

export async function fetchPostsData(): Promise<FeedData> {
  return fetch("/api/feed")
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
    });
}
