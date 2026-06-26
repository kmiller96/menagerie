"use server";

import { revalidatePath } from "next/cache";
import { createNote } from "./db";

export async function createNoteAction(formData: FormData) {
  const content = formData.get("content") as string;
  if (!content?.trim()) return;
  createNote(content.trim());
  revalidatePath("/");
}
