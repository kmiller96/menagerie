import dotenv from 'dotenv';

import { streamText } from "ai";
import { openai } from "@ai-sdk/openai";

dotenv.config();  // Load the `.env` file

let model = openai("gpt-5.2");
let prompt = "Invent a new holiday and describe its traditions.";

console.log("Generating text for prompt:", prompt, "\n\n");

const { textStream } = streamText({ model, prompt });

for await (const chunk of textStream) {
  process.stdout.write(chunk);
}
