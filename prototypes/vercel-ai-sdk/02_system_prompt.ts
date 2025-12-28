import dotenv from 'dotenv';

import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

dotenv.config();  // Load the `.env` file

let model = openai("gpt-5.2");
let system = "You are a dog. You should only respond with dog sounds.";
let prompt = "What is love?";

console.log("Generating text for prompt:", prompt, "\n\n");

const { text } = await generateText({ model, system, prompt });

console.log("Response:", text);