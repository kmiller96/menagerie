import dotenv from "dotenv";

import { streamText, Output } from "ai";
import { openai } from "@ai-sdk/openai";

dotenv.config({ quiet: true }); // Load the `.env` file

const model = openai("gpt-5-mini");
const prompt = "This resturant was SO GOOD. I love waiting hours for food!";

// NOTE: We can use `generateText` here as well for non-streaming structured outputs
const { textStream } = streamText({
  model,
  prompt,
  system:
    "Classify this text as being either positive, negative, or neutral in sentiment.",
  output: Output.choice({ options: ["positive", "negative", "neutral"] }),
});

for await (const chunk of textStream) {
  process.stdout.write(chunk);
}
