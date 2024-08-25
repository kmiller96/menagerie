# My Auth

An attempt to make my own basic authentication. This is to help me internalise
how auth works and the value of using an existing tool (because the all seem so
bloody complicated!!)

## Basic Design

We are going to try to implement a "naive" implementation without consulting
any online materials. This will give us a firm grounding to help better
internalise why authentication is done the way it is done.

We are going to start with a really simple session-based authentication. The idea
will be like so:

1. The user will login with a username and password.
2. The server will validate these credentials.
3. If mismatch, reject (maybe a 400 error?).
4. If match:
   1. Create a new user session.
   2. Send the session back to the user as a cookie.

On subsequent requests, the workflow will then look like so:

1. Receive request.
2. For protected endpoints, attempt to extract the session ID from the cookie.
3. If no cookie, reject and redirect.
4. If cookie, validate against current sessions.
