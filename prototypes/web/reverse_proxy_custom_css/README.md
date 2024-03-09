# Reverse Proxy Custom CSS

Showcase how you can inject in your own stylesheets for a domain.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
bash run.sh
```

## Retrospective

So it _almost_ worked, but not quite. I couldn't quite get the images to work,
and the rendered URLs of subpages are wrong, but they are easily fixable with
a bit of work and effort.

### Alternative Approaches

A really simple approach to this problem would be to export all of the content
as markdown and then render it on our side.

We could also do the same approach but instead "crawl" our Notion content and get
the rendered HTML, which we could then again restyle with some simple CSS.

Another approach would be follow a solution from someone else and try to get
that to work. For example:

- https://forum.level1techs.com/t/infrastructure-series-use-nginx-to-inject-css-themes/174165/2
- https://github.com/equiposinoficina/notion-proxy-ng

## Improvements

You could switch this slow, python implementation out for one of the following:

- A very fast Caddy/NGINX implementation.
- A rust implementation.
