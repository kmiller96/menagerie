"""The 'Hello World' of LangChain."""

import os

from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI

# ------------------ #
# -- Load API Key -- #
# ------------------ #

with open("chatgpt.key", "r") as f:
    api_key = f.read().strip()

with open("langsmith.key", "r") as f:
    langsmith_key = f.read().strip()

# ------------------------------- #
# -- Set Environment Variables -- #
# ------------------------------- #

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = langsmith_key
os.environ["LANGCHAIN_PROJECT_ID"] = "pr-monthly-restoration-24"


# ----------------- #
# -- Run Example -- #
# ----------------- #

model = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

template = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the following from English into {language}"),
        ("user", "{text}"),
    ]
)

prompt = template.invoke({"language": "Italian", "text": "How are you?"})
result = model.invoke(prompt)
print(result)
