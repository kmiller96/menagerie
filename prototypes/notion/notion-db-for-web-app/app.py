import asyncio

import fastapi
from notion_client import AsyncClient

#############
## Globals ##
#############

DATABASE_ID = "15a57f7b16424efb940dbe8c6346e883"  # Projects DB


#####################
## Database Client ##
#####################


class DatabaseClient:
    """Abstracts away Notion and provides a standard database client interface."""

    def __init__(self, api_key: str, database_id: str):
        self.client = AsyncClient(auth=api_key)
        self.database_id = database_id

    async def info(self):
        """Returns information about a database."""
        return await self.client.databases.retrieve(self.database_id)

    async def query(
        self,
        filter=None,
        sorts=None,
        start_cursor: None | str = None,
        page_size: int = 100,
    ):
        """Returns a list of pages in a database."""
        kwargs = {}

        if filter:
            kwargs["filter"] = filter
        if sorts:
            kwargs["sorts"] = sorts
        if start_cursor:
            kwargs["start_cursor"] = start_cursor

        return await self.client.databases.query(
            self.database_id,
            page_size=page_size,
            **kwargs,
        )

    async def get(self, id: str):
        """Returns a single row in the database by ID."""
        page_promise = self.client.pages.retrieve(id)
        content_promise = self.client.blocks.children.list(id)

        page, content = await asyncio.gather(page_promise, content_promise)

        return {
            "page": page,
            "content": content,
        }


###########################
## Initialised DB Client ##
###########################

with open("SECRET") as f:
    api_key = f.read().strip()

db = DatabaseClient(
    api_key=api_key,
    database_id=DATABASE_ID,
)


############
## Routes ##
############


api = fastapi.FastAPI()


@api.get("/")
async def index():
    """Returns a list of pages in the database."""
    results = await db.query()
    return results


@api.get("/{id}")
async def get_page(id: str):
    """Returns a single page by ID."""
    return await db.get(id)
