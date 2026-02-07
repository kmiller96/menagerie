import { describe, expect, it } from "vitest";
import { isValidHttpUrl } from "@/lib/validation/url";

describe("isValidHttpUrl", () => {
  it("accepts absolute http and https urls", () => {
    expect(isValidHttpUrl("http://example.com")).toBe(true);
    expect(isValidHttpUrl("https://example.com/path?q=1")).toBe(true);
  });

  it("rejects invalid or unsupported urls", () => {
    expect(isValidHttpUrl("foo")).toBe(false);
    expect(isValidHttpUrl("javascript:alert(1)")).toBe(false);
    expect(isValidHttpUrl("ftp://example.com")).toBe(false);
  });
});
