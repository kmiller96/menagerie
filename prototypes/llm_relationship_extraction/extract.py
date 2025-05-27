import asyncio
import re
import sys
import argparse
from textwrap import dedent

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

#############
## Helpers ##
#############


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract Cypher queries from a web page or text snippet."
    )
    parser.add_argument(
        "input", type=str, help="The URL of the web page or text snippet to analyze."
    )
    return parser.parse_args()


def execute_cypher_query(query):
    """
    Placeholder function to execute the Cypher query.
    This function should connect to a Neo4j database and execute the provided query.
    """
    # Implementation for executing the Cypher query goes here
    # For now, we will just print the query
    print(query)


##################
## Main Routine ##
##################


async def main():
    ## Parse args ##
    args = parse_args()

    ## Submit task ##
    response = client.responses.create(
        model="gpt-4o",
        instructions=dedent("""
            You are an expert in Neo4j Cypher and you will be given a task to extract 
            entities and relationships. You will be supplied with either a web page
            or a snippet of text. Your task is to write a Cypher query that inserts 
            the extracted data into a Neo4j database.
                            
            Do not include anything except for the Cypher query in your response.

            If you cannot find any entities or relationships, return an empty string
            within a code block, like this:

            ```cypher
            ```
        """),
        tools=[{"type": "web_search_preview"}],
        input=args.input,
    )

    pattern = r"```(?:\w+\n)?(.*?)```"
    matches = re.findall(pattern, response.output_text, re.DOTALL)

    if matches:
        for i, match in enumerate(matches):
            execute_cypher_query(match.strip())
    else:
        print("[ERROR] No Cypher query found in the response.", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
