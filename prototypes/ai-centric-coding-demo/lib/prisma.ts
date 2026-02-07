import { PrismaLibSql } from "@prisma/adapter-libsql";
import { PrismaClient } from "@prisma/client";
import { env } from "@/lib/env";

declare global {
  var prisma: PrismaClient | undefined;
}

export const prisma =
  global.prisma ??
  new PrismaClient({
    adapter: new PrismaLibSql({
      url: env.DATABASE_URL,
    }),
  });

if (process.env.NODE_ENV !== "production") {
  global.prisma = prisma;
}
