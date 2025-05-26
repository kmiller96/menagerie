import asyncio

from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")


async def main():
    agent = Agent(
        task="Summarise the top links from Hacker News.",
        llm=llm,
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
