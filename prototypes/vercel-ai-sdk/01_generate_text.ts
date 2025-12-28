import dotenv from 'dotenv';

import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

dotenv.config();  // Load the `.env` file

let model = openai("gpt-5.2");
let prompt = "What is love?";

console.log("Generating text for prompt:", prompt, "\n\n");

const { text } = await generateText({ model, prompt });

console.log("Response:", text);