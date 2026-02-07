const databaseUrl = process.env.DATABASE_URL;

if (!databaseUrl) {
  throw new Error(
    "Missing DATABASE_URL. Set it in your environment before starting the app.",
  );
}

export const env = {
  DATABASE_URL: databaseUrl,
} as const;
