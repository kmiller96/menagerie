import dotenv from 'dotenv';

import { generateText, type ModelMessage } from "ai";
import { openai } from "@ai-sdk/openai";

dotenv.config({quiet: true});  // Load the `.env` file

const model = openai("gpt-5-mini");
const prompt = "Invent a new holiday and describe its traditions.";

const messages: ModelMessage[] = [
  { role: "user", content: prompt }
];

console.log("Performing turn 1.")

const { text } = await generateText({ model, messages });
messages.push({ role: "assistant", content: text });


let followUp = "What foods are typically eaten during this holiday?";
messages.push({ role: "user", content: followUp });

console.log("Performing turn 2.")
const { text: followUpResponse } = await generateText({ model, messages });

console.log("Follow up Response:", followUpResponse);

