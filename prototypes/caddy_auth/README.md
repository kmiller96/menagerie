# Caddy Auth

Playing around with installing a global authentication layer into Caddy.

## Running The Server

```bash
make run
```

## Learnings

Okay so adding OAuth continues to be a huge headache for me. Why is it so hard?

All my initial poking around seems to want you to put it at the application
level, not the reverse proxy level, yet lots of resources online tell you "make
sure you put authentication on the reverse proxy!". So I'm all a big confused as
to what approach is the right approach.

But I guess this is just if you want SSO on all your applications. If you're
happy with the user having to authenticate separately on both apps, then you
can probably get away with just doing it at an application level.

My understanding is that if you want to go with an SSO option, you'd deploy a
single authentication service to handle authentication/authorization across all
of your apps and just have them all verify tokens. E.g. you would end up using
a server like [keycloak](https://www.keycloak.org/).
