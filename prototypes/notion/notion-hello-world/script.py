import asyncio
import pprint

from notion_client import AsyncClient

# ---------- #
# -- Main -- #
# ---------- #


async def main():
    # -- Authenticate -- #
    client = AsyncClient(auth=load_secret())

    # -- Get Users -- #
    users = await client.users.list()
    pprint.pp(users)

    # -- Load Page -- #
    page = await client.pages.retrieve("78ed0120dc8549958b4028d2e47c0be6")
    pprint.pp(page)


# ----------------- #
# -- Subroutines -- #
# ----------------- #


def load_secret():
    with open("SECRET") as f:
        return f.read().strip()


if __name__ == "__main__":
    asyncio.run(main())
