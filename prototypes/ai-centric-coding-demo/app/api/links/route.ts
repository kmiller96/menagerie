import { Prisma } from "@prisma/client";
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { createWithGeneratedSlug } from "@/lib/slug";
import { isValidHttpUrl } from "@/lib/validation/url";

const DEFAULT_LIMIT = 20;
const MAX_LIMIT = 100;

type LinkCreateResponse = {
  id: string;
  slug: string;
  shortUrl: string;
  targetUrl: string;
  createdAt: string;
};

type LinkListResponse = Array<{
  id: string;
  slug: string;
  targetUrl: string;
  createdAt: string;
  clickCount: number;
}>;

function isUniqueConstraintError(error: unknown): boolean {
  return (
    error instanceof Prisma.PrismaClientKnownRequestError &&
    error.code === "P2002"
  );
}

function parseLimit(rawLimit: string | null): number | null {
  if (!rawLimit) {
    return DEFAULT_LIMIT;
  }

  const limit = Number.parseInt(rawLimit, 10);

  if (!Number.isFinite(limit) || limit < 1) {
    return null;
  }

  return Math.min(limit, MAX_LIMIT);
}

export async function POST(request: NextRequest) {
  let body: unknown;

  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "Invalid JSON body." }, { status: 400 });
  }

  const url =
    typeof body === "object" && body !== null && "url" in body
      ? (body.url as unknown)
      : null;

  if (typeof url !== "string" || !isValidHttpUrl(url)) {
    return NextResponse.json(
      { error: "Invalid URL. Use an absolute http/https URL." },
      { status: 400 },
    );
  }

  try {
    const created = await createWithGeneratedSlug({
      create: async (slug) =>
        prisma.link.create({
          data: {
            slug,
            targetUrl: url,
          },
        }),
      isCollisionError: isUniqueConstraintError,
    });

    if (!created) {
      return NextResponse.json(
        { error: "Failed to generate a unique slug." },
        { status: 500 },
      );
    }

    const response: LinkCreateResponse = {
      id: created.id,
      slug: created.slug,
      shortUrl: `${request.nextUrl.origin}/s/${created.slug}`,
      targetUrl: created.targetUrl,
      createdAt: created.createdAt.toISOString(),
    };

    return NextResponse.json(response, { status: 201 });
  } catch {
    return NextResponse.json(
      { error: "Failed to create short link." },
      { status: 500 },
    );
  }
}

export async function GET(request: NextRequest) {
  const limit = parseLimit(request.nextUrl.searchParams.get("limit"));

  if (!limit) {
    return NextResponse.json(
      { error: "Invalid limit. Use a positive integer." },
      { status: 400 },
    );
  }

  const links = await prisma.link.findMany({
    orderBy: {
      createdAt: "desc",
    },
    take: limit,
    select: {
      id: true,
      slug: true,
      targetUrl: true,
      createdAt: true,
      clickCount: true,
    },
  });

  const response: LinkListResponse = links.map((link) => ({
    ...link,
    createdAt: link.createdAt.toISOString(),
  }));

  return NextResponse.json(response);
}
