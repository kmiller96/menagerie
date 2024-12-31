"""The 'Hello World' of LangChain."""

import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


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

os.environ["OPENAI_API_KEY"] = api_key

# ----------------- #
# -- Run Example -- #
# ----------------- #

# Init components
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
model = ChatOpenAI(model="gpt-4o-mini")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True,
)

# Load document & split into chunks
print("Loading document...")
loader = PyPDFLoader("./nke-10k-2023.pdf")
docs = loader.load()
print("Splitting document...")
splits = splitter.split_documents(docs)

# Embed chunks
print("Embedding chunks...")
vector_store = InMemoryVectorStore(embeddings)
ids = vector_store.add_documents(documents=splits)

# Test similarity search
print("Asking question...")
results = vector_store.similarity_search_with_score("When was nike incorporated?")

print(results[0])
