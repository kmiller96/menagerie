import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaLibSql } from "@prisma/adapter-libsql";
import { PrismaClient } from "@prisma/client";
import { env } from "@/lib/env";

declare global {
  var prisma: PrismaClient | undefined;
}

const adapter = env.DATABASE_URL.startsWith("postgres")
  ? new PrismaPg({ connectionString: env.DATABASE_URL })
  : new PrismaLibSql({ url: env.DATABASE_URL });

export const prisma =
  global.prisma ??
  new PrismaClient({
    adapter,
  });

if (process.env.NODE_ENV !== "production") {
  global.prisma = prisma;
}
