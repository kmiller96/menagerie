export const SLUG_LENGTH = 7;
export const DEFAULT_MAX_SLUG_RETRIES = 5;

const SLUG_ALPHABET =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

type GetRandomValues = (array: Uint8Array) => Uint8Array;

type CreateWithGeneratedSlugOptions<T> = {
  create: (slug: string) => Promise<T>;
  isCollisionError: (error: unknown) => boolean;
  maxRetries?: number;
  generate?: () => string;
};

export function generateSlug(getRandomValues: GetRandomValues = crypto.getRandomValues.bind(crypto)): string {
  const randomBytes = getRandomValues(new Uint8Array(SLUG_LENGTH));

  return Array.from(
    randomBytes,
    (value) => SLUG_ALPHABET[value % SLUG_ALPHABET.length],
  ).join("");
}

export async function createWithGeneratedSlug<T>({
  create,
  isCollisionError,
  maxRetries = DEFAULT_MAX_SLUG_RETRIES,
  generate = generateSlug,
}: CreateWithGeneratedSlugOptions<T>): Promise<T | null> {
  for (let attempt = 0; attempt < maxRetries; attempt += 1) {
    try {
      return await create(generate());
    } catch (error) {
      if (isCollisionError(error)) {
        continue;
      }

      throw error;
    }
  }

  return null;
}
