"""The 'Hello World' of LangChain."""

from langchain_core.messages import HumanMessage, SystemMessage

from langchain_openai import ChatOpenAI

with open("chatgpt.key", "r") as f:
    api_key = f.read().strip()

model = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

##############################
## Example 1: Basic Request ##
##############################

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

result = model.invoke(messages)
print(result)

##########################
## Example 2: Streaming ##
##########################

for token in model.stream(messages):
    print(token.content, end="|")
