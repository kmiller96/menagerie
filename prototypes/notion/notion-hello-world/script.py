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

    # -- Print -- #
    pprint.pp(users)


# ----------------- #
# -- Subroutines -- #
# ----------------- #


def load_secret():
    with open("SECRET") as f:
        return f.read().strip()


if __name__ == "__main__":
    asyncio.run(main())
