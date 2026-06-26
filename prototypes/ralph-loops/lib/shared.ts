export interface Note {
  id: number;
  body: string;
  created_at: string;
  updated_at: string;
}

// Capturing group so split() in client components preserves tag delimiters
export const TAG_PATTERN = /(#[\w-]+)/gi;

/** Format a date string as a human-friendly relative time. */
export function timeAgo(dateStr: string): string {
  const now = Date.now();
  const date = new Date(
    dateStr.endsWith("Z") ? dateStr : `${dateStr}Z`,
  ).getTime();
  const diff = now - date;
  const minutes = Math.floor(diff / 60000);
  if (minutes < 1) return "just now";
  if (minutes < 60) return `${minutes} min ago`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `${hours} hr ago`;
  const days = Math.floor(hours / 24);
  return `${days} day${days > 1 ? "s" : ""} ago`;
}
