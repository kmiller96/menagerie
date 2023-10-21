# Download Notion

Prototype showcasing how to download pages from Notion.

## Setup

1. Create an integration on Notion.
2. Get the secret and save it into a file called `secret.txt` (this file is 
   ignored in the git history).
3. Navigate to Notion and authorize the integration to access the page you wish
   to download via `... --> Add connections --> <connection name>`
4. Create a virutal environment (`python -m venv .venv`), activate it 
   (`source .venv/bin/activate`) and install the necessary dependencies 
   (`pip install -r requirements.txt`).
5. Run the application.

## Usage

```bash
python run.py <notion url> 
```

This will print the response to STDOUT. This can then be redirected into a file 
or piped to another application. For example:

```bash
python run.py \
   https://www.notion.so/Notion-Markdown-Example-421e9202cd2d485997a345ebfa90123c \
   > result.json
```

This output is deliberated printed out as a single line to make it easier to 
append to a JSONLines file. If you wish to pretty print, I recommend you run
something like this:

```bash
python run.py https://www.notion.so/Notion-Markdown-Example-421e9202cd2d485997a345ebfa90123c \
| python -m json.tool \
> result.json
```

## Limitations

I believe that this request isn't _recursive_. That is, you couldn't retreive any
nested content (e.g. a database within the page, a page within a page, etc.) so
this doesn't work in all occurances.

There is an endpoint called [append block children](https://developers.notion.com/reference/patch-block-children)
which might do some of the desired behaviour, but I didn't explore this.
