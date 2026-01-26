# Mail-to-API

Server that watches an SMTP mail server for new emails, forwarding them to an
API.

## Why?

Sometimes it would be handy if you could just interact with a service via email.
Trigger on emai? Yes please. Send an attachment, get it loaded into a data
warehouse? Imagine that!

In theory it could be a micro SaaS if it was a real niche in the industry. I
think it's valuable. Maybe others would too? Especially with a PAYG credit
system or reasonable usage tiers. Hell, even on-prem deployments would be handy
for big orgs...

## Quickstart

> [!NOTE]
> It is essential that you have an App Password setup with Gmail!

1. Create an App password
2. Set the `EMAIL_USER` and `EMAIL_PASS` environment variables (or set a `.env` file).
3. `uv run main.py`

## Extensions

### Self-Hosted Mail Server for Many Users

I've run this prototype using Gmail because it's simple and easy. But if you
wanted separate destinations (e.g. per user) you would probably want to run your
own mail server instead.

I saw this docker image which was interesting:
https://docker-mailserver.github.io/docker-mailserver/latest/.
