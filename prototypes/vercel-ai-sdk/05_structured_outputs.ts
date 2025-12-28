import dotenv from "dotenv";

import { streamText, Output } from "ai";
import { openai } from "@ai-sdk/openai";

import { z } from "zod";

dotenv.config({ quiet: true }); // Load the `.env` file

const schema = z.object({
  recipe: z.object({
    name: z.string().describe("The name of the recipe"),
    ingredients: z.array(
      z
        .object({
          name: z.string(),
          quantity: z.string(),
        })
        .describe("The ingredients needed for the recipe")
    ),
    steps: z.array(z.string()).describe("The steps to prepare the recipe"),
  }),
});

const model = openai("gpt-5-mini");
const prompt =
  "Give me a recipe for a spaghetti bolognese using lentils instead of minced meat.";

// NOTE: We can use `generateText` here as well for non-streaming structured outputs
const { textStream } = await streamText({
  model,
  prompt,
  system:
    "You are a helpful assistant that provides recipes in a structured format.",
  output: Output.object({ schema, name: "Recipe" }),
});

for await (const chunk of textStream) {
  process.stdout.write(chunk);
}
