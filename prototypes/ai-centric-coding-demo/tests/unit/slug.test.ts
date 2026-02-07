import { describe, expect, it } from "vitest";
import { createWithGeneratedSlug, generateSlug, SLUG_LENGTH } from "@/lib/slug";

describe("generateSlug", () => {
  it("returns a 7-character base62 slug", () => {
    const slug = generateSlug((array) => {
      for (let index = 0; index < array.length; index += 1) {
        array[index] = index;
      }
      return array;
    });

    expect(slug).toHaveLength(SLUG_LENGTH);
    expect(slug).toMatch(/^[A-Za-z0-9]{7}$/);
  });
});

describe("createWithGeneratedSlug", () => {
  it("retries on collisions and eventually succeeds", async () => {
    const generated = ["aaaaaaa", "bbbbbbb", "ccccccc"];
    let attempt = 0;

    const created = await createWithGeneratedSlug({
      generate: () => generated[attempt++] || "zzzzzzz",
      create: async (slug) => {
        if (slug !== "ccccccc") {
          throw new Error("collision");
        }

        return { slug };
      },
      isCollisionError: (error) => error instanceof Error && error.message === "collision",
      maxRetries: 5,
    });

    expect(created).toEqual({ slug: "ccccccc" });
    expect(attempt).toBe(3);
  });

  it("returns null when collisions exceed retry limit", async () => {
    const created = await createWithGeneratedSlug({
      generate: () => "aaaaaaa",
      create: async () => {
        throw new Error("collision");
      },
      isCollisionError: (error) => error instanceof Error && error.message === "collision",
      maxRetries: 2,
    });

    expect(created).toBeNull();
  });
});
