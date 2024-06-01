# FastAPI Session Auth

Prototype showing how you can roll your own (simple) session-based authentication
using cookies

## Why?

I keep wanting to add authentication to my applications, but I really cbf 
learning a heavy plugin like `fastapi-users`. I'm sure after you learn the plugin
it's simple. However, for a first pass, it definitely seems like overkill.

I want to validate this assumption using a prototype of my own, as well as figure 
out how I can roll my own authentication if I decide to do so.

## Learnings

Okay, so perhaps the plugins have some merit to them. There is, surprisingly, 
quite a lot of supporting code that needs to be put in place for authentication
to work. And this is for a very simple authentication scheme.

For simple, API-key based APIs, you could probably use a library like 
[this one](https://github.com/mrtolkien/fastapi_simple_security). For more 
complex APIs, such as for proper web applications, it looks like 
[FastAPI Users](https://fastapi-users.github.io/fastapi-users/latest/) has the 
most support.

Here is a good idiot's guide to using FastAPI users with SQLModel: 
https://medium.com/@kasperjuunge/how-to-use-fastapi-users-cae8ed1058f8