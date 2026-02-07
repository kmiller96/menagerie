import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export const runtime = "nodejs";

type RouteContext = {
  params: Promise<{
    slug: string;
  }>;
};

export async function GET(_request: NextRequest, context: RouteContext) {
  const { slug } = await context.params;

  const targetUrl = await prisma.$transaction(async (tx) => {
    const link = await tx.link.findUnique({
      where: { slug },
      select: {
        id: true,
        targetUrl: true,
      },
    });

    if (!link) {
      return null;
    }

    await tx.link.update({
      where: { id: link.id },
      data: {
        clickCount: {
          increment: 1,
        },
      },
    });

    await tx.clickEvent.create({
      data: {
        linkId: link.id,
      },
    });

    return link.targetUrl;
  });

  if (!targetUrl) {
    return new NextResponse("Not Found", { status: 404 });
  }

  return NextResponse.redirect(targetUrl, { status: 307 });
}
