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

## Lessons

This was, in fact, actually pretty easy to do! And having AI do the heavy
lifting of parsing the emails themselves helped a lot in pulling this prototype
together ASAP.

I think this is a valuable service, albeit a niche one. Definitely an
interesting concept for an application. I do believe that people would want to
use a service like this, but it would require a lot of marketing just so people
know that it even exists. Maybe one day when I'm bored... but I doubt I'll ever
want to work on it.

I think the right way to approach this would be a very simple web app to allow
users to configure the service to their needs. Then this code here forms the
core of the IP which is the email service handler.

If you, random poke-arounder of this repo want to steal this idea I encourage
you to do so. Offer a free tier with something like 10 emails per month for one
address. Require users sign up with an SSO service to prevent spam. Have zero
onboarding effort by you for these free users. Offer a paid tier of something
like US$5pm for "fair usage". That could be a very reasonable amount of like
1000 emails per day (it will still be a small impact on your servers). Offer
an enterprise tier for users who want on-prem, their own domains, etc.

If you did decide to go on-prem you might want to investigate not using python
or obfuscating the code so they can't tamper with it too much.

## Extensions

### Self-Hosted Mail Server for Many Users

I've run this prototype using Gmail because it's simple and easy. But if you
wanted separate destinations (e.g. per user) you would probably want to run your
own mail server instead.

I saw this docker image which was interesting:
https://docker-mailserver.github.io/docker-mailserver/latest/.
