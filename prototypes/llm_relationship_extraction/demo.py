import re
from textwrap import dedent

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    instructions=dedent("""
        You are an expert in Neo4j Cypher and you will be given a task to extract 
        entities and relationships. You will be supplied with either a web page
        or a snippet of text. Your task is to write a Cypher query that inserts 
        the extracted data into a Neo4j database.
                        
        Do not include anything except for the Cypher query in your response.
    """),
    tools=[{"type": "web_search_preview"}],
    input="https://en.wikipedia.org/wiki/Cypherpunk",
)

text = response.output_text

pattern = r"```(?:\w+\n)?(.*?)```"
matches = re.findall(pattern, text, re.DOTALL)

if matches:
    for i, match in enumerate(matches):
        print(match.strip())
else:
    print("No Cypher query found in the response.")
