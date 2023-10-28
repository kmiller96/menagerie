# ChatGPT Editor

Edits a blog article for you using ChatGPT.

## Reviewing Spelling & Grammar

```bash
export OPENAI_SECRET=$(cat secret.txt)
python scripts/edit.py article.md
```

## Reorganising Content

```bash
export OPENAI_SECRET=$(cat secret.txt)
python scripts/reword.py article.md
```

## Recommending Changes 

```bash
export OPENAI_SECRET=$(cat secret.txt)
python scripts/suggest.py article.md
```