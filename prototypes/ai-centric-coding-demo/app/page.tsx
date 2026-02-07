"use client";

import { FormEvent, useEffect, useMemo, useState } from "react";

type LinkListItem = {
  id: string;
  slug: string;
  targetUrl: string;
  createdAt: string;
  clickCount: number;
};

type CreatedLink = {
  id: string;
  slug: string;
  shortUrl: string;
  targetUrl: string;
  createdAt: string;
};

const DATE_FORMATTER = new Intl.DateTimeFormat(undefined, {
  dateStyle: "medium",
  timeStyle: "short",
});

function formatTimestamp(value: string): string {
  const parsed = new Date(value);

  if (Number.isNaN(parsed.getTime())) {
    return value;
  }

  return DATE_FORMATTER.format(parsed);
}

export default function Home() {
  const [url, setUrl] = useState("");
  const [links, setLinks] = useState<LinkListItem[]>([]);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isLoadingLinks, setIsLoadingLinks] = useState(true);
  const [createError, setCreateError] = useState<string | null>(null);
  const [listError, setListError] = useState<string | null>(null);
  const [createdLink, setCreatedLink] = useState<CreatedLink | null>(null);
  const [copyState, setCopyState] = useState<"idle" | "copied" | "failed">(
    "idle",
  );

  const createdAtLabel = useMemo(
    () => (createdLink ? formatTimestamp(createdLink.createdAt) : null),
    [createdLink],
  );

  async function loadLinks() {
    setIsLoadingLinks(true);
    setListError(null);

    try {
      const response = await fetch("/api/links?limit=20", {
        method: "GET",
      });

      if (!response.ok) {
        const payload = (await response.json().catch(() => null)) as
          | { error?: string }
          | null;
        throw new Error(payload?.error ?? "Failed to load links.");
      }

      const payload = (await response.json()) as LinkListItem[];
      setLinks(payload);
    } catch (error) {
      setListError(
        error instanceof Error ? error.message : "Failed to load links.",
      );
    } finally {
      setIsLoadingLinks(false);
    }
  }

  useEffect(() => {
    void loadLinks();
  }, []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setCreateError(null);
    setCopyState("idle");
    setIsSubmitting(true);

    try {
      const response = await fetch("/api/links", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const payload = (await response.json().catch(() => null)) as
        | CreatedLink
        | { error?: string }
        | null;

      if (!response.ok) {
        throw new Error(
          payload && "error" in payload && payload.error
            ? payload.error
            : "Failed to create short link.",
        );
      }

      setCreatedLink(payload as CreatedLink);
      setUrl("");
      await loadLinks();
    } catch (error) {
      setCreateError(
        error instanceof Error ? error.message : "Failed to create short link.",
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  async function handleCopy() {
    if (!createdLink) {
      return;
    }

    try {
      await navigator.clipboard.writeText(createdLink.shortUrl);
      setCopyState("copied");
    } catch {
      setCopyState("failed");
    }
  }

  return (
    <main className="mx-auto flex min-h-screen w-full max-w-4xl flex-col gap-10 px-6 py-12">
      <section className="space-y-3">
        <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
          Link Shortener MVP
        </p>
        <h1 className="text-3xl font-semibold text-slate-900">
          Create short links and track clicks
        </h1>
        <p className="text-slate-600">
          Paste a full URL (`http` or `https`), generate a short link, then
          monitor recent traffic.
        </p>
      </section>

      <section className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <form className="space-y-4" onSubmit={handleSubmit}>
          <label className="block text-sm font-medium text-slate-700" htmlFor="url">
            Destination URL
          </label>
          <div className="flex flex-col gap-3 sm:flex-row">
            <input
              id="url"
              type="url"
              value={url}
              onChange={(event) => setUrl(event.target.value)}
              placeholder="https://example.com"
              required
              className="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none transition focus:border-slate-500"
            />
            <button
              type="submit"
              disabled={isSubmitting}
              className="rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {isSubmitting ? "Creating..." : "Create link"}
            </button>
          </div>
        </form>

        {createError ? (
          <p className="mt-4 rounded-lg border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
            {createError}
          </p>
        ) : null}

        {createdLink ? (
          <div className="mt-4 rounded-lg border border-emerald-200 bg-emerald-50 p-4">
            <p className="text-sm font-medium text-emerald-900">Short link created</p>
            <div className="mt-2 flex flex-col gap-2 sm:flex-row sm:items-center">
              <a
                href={createdLink.shortUrl}
                target="_blank"
                rel="noreferrer"
                className="break-all text-sm font-medium text-emerald-900 underline"
              >
                {createdLink.shortUrl}
              </a>
              <button
                type="button"
                onClick={handleCopy}
                className="rounded-md border border-emerald-400 px-3 py-1 text-xs font-medium text-emerald-900"
              >
                Copy
              </button>
            </div>
            <p className="mt-1 text-xs text-emerald-800">
              Created {createdAtLabel} for {createdLink.targetUrl}
            </p>
            {copyState === "copied" ? (
              <p className="mt-2 text-xs text-emerald-900">Copied to clipboard.</p>
            ) : null}
            {copyState === "failed" ? (
              <p className="mt-2 text-xs text-amber-900">
                Could not copy automatically. Copy the link manually.
              </p>
            ) : null}
          </div>
        ) : null}
      </section>

      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-semibold text-slate-900">Recent links</h2>
          <button
            type="button"
            onClick={() => void loadLinks()}
            disabled={isLoadingLinks}
            className="rounded-md border border-slate-300 px-3 py-1.5 text-sm text-slate-700 disabled:opacity-60"
          >
            Refresh
          </button>
        </div>

        {listError ? (
          <p className="rounded-lg border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
            {listError}
          </p>
        ) : null}

        {isLoadingLinks ? (
          <p className="text-sm text-slate-500">Loading recent links...</p>
        ) : null}

        {!isLoadingLinks && links.length === 0 ? (
          <p className="text-sm text-slate-500">No links yet.</p>
        ) : null}

        {!isLoadingLinks && links.length > 0 ? (
          <ul className="divide-y divide-slate-200 rounded-xl border border-slate-200 bg-white">
            {links.map((link) => (
              <li key={link.id} className="space-y-1 p-4">
                <div className="flex flex-col justify-between gap-2 sm:flex-row sm:items-center">
                  <a
                    href={`/s/${link.slug}`}
                    target="_blank"
                    rel="noreferrer"
                    className="font-medium text-slate-900 underline"
                  >
                    /s/{link.slug}
                  </a>
                  <span className="text-sm text-slate-600">
                    {link.clickCount} {link.clickCount === 1 ? "click" : "clicks"}
                  </span>
                </div>
                <p className="break-all text-sm text-slate-700">{link.targetUrl}</p>
                <p className="text-xs text-slate-500">
                  Created {formatTimestamp(link.createdAt)}
                </p>
              </li>
            ))}
          </ul>
        ) : null}
      </section>
    </main>
  );
}
