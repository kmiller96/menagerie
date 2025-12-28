import dotenv from "dotenv";

import { streamText, tool } from "ai";
import { openai } from "@ai-sdk/openai";

import { z } from "zod";

dotenv.config({ quiet: true }); // Load the `.env` file

// -- Tools -------------------------------------------------------------------

const printToTerminal = tool({
  description: "Prints a message to the terminal",
  inputSchema: z.object({
    message: z.string(),
  }),
  execute: async ({ message }) => {
    console.log(message);
  },
});

// -- Prompt ------------------------------------------------------------------

const model = openai("gpt-5-mini");
const prompt = "Hello World!";

// NOTE: We can use `generateText` here as well for non-streaming structured outputs
const { textStream, steps } = streamText({
  model,
  prompt,
  system:
    "Whatever the user says, print it to the terminal using the tool provided.",
  tools: {
    printToTerminal,
  },
});

for await (const chunk of textStream) {
  process.stdout.write(chunk);
}

console.log("\n\nTool Execution Steps:\n", await steps);
