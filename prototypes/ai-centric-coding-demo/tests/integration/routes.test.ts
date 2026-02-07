import { afterAll, beforeEach, describe, expect, it } from "vitest";
import { NextRequest } from "next/server";
import { prisma } from "@/lib/prisma";
import { GET as getLinks, POST } from "@/app/api/links/route";
import { GET as redirect } from "@/app/s/[slug]/route";

beforeEach(async () => {
  await prisma.clickEvent.deleteMany();
  await prisma.link.deleteMany();
});

afterAll(async () => {
  await prisma.$disconnect();
});

describe("POST /api/links", () => {
  it("creates a short link for a valid URL", async () => {
    const request = new NextRequest("http://localhost/api/links", {
      method: "POST",
      body: JSON.stringify({ url: "https://example.com" }),
      headers: {
        "content-type": "application/json",
      },
    });

    const response = await POST(request);
    const data = (await response.json()) as {
      id: string;
      slug: string;
      shortUrl: string;
      targetUrl: string;
      createdAt: string;
    };

    expect(response.status).toBe(201);
    expect(data.slug).toMatch(/^[A-Za-z0-9]{7}$/);
    expect(data.shortUrl).toBe(`http://localhost/s/${data.slug}`);
    expect(data.targetUrl).toBe("https://example.com");

    const stored = await prisma.link.findUnique({ where: { id: data.id } });
    expect(stored?.targetUrl).toBe("https://example.com");
  });

  it("rejects invalid URLs", async () => {
    const request = new NextRequest("http://localhost/api/links", {
      method: "POST",
      body: JSON.stringify({ url: "javascript:alert(1)" }),
      headers: {
        "content-type": "application/json",
      },
    });

    const response = await POST(request);
    const data = (await response.json()) as { error: string };

    expect(response.status).toBe(400);
    expect(data.error).toMatch(/Invalid URL/);
  });
});

describe("GET /s/{slug}", () => {
  it("redirects and records click analytics", async () => {
    const link = await prisma.link.create({
      data: {
        slug: "abc1234",
        targetUrl: "https://example.org",
      },
    });

    const response = await redirect(new NextRequest("http://localhost/s/abc1234"), {
      params: Promise.resolve({ slug: "abc1234" }),
    });

    expect(response.status).toBe(307);
    expect(response.headers.get("location")).toBe("https://example.org/");

    const updated = await prisma.link.findUnique({ where: { id: link.id } });
    expect(updated?.clickCount).toBe(1);

    const clickEvents = await prisma.clickEvent.count({ where: { linkId: link.id } });
    expect(clickEvents).toBe(1);
  });

  it("returns 404 for unknown slugs", async () => {
    const response = await redirect(new NextRequest("http://localhost/s/missing12"), {
      params: Promise.resolve({ slug: "missing12" }),
    });

    expect(response.status).toBe(404);
  });
});

describe("GET /api/links", () => {
  it("returns links newest-first", async () => {
    await prisma.link.create({
      data: {
        slug: "oldlink1",
        targetUrl: "https://old.example",
        createdAt: new Date("2026-01-01T00:00:00.000Z"),
      },
    });

    await prisma.link.create({
      data: {
        slug: "newlink1",
        targetUrl: "https://new.example",
        createdAt: new Date("2026-01-02T00:00:00.000Z"),
      },
    });

    const response = await getLinks(new NextRequest("http://localhost/api/links?limit=20"));
    const data = (await response.json()) as Array<{ slug: string }>;

    expect(response.status).toBe(200);
    expect(data.map((item) => item.slug)).toEqual(["newlink1", "oldlink1"]);
  });
});
