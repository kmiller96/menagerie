# Chatroom

Implements a chatroom in basic TCP.

To start the chatroom server:

```bash
<program> server
```

To initiate a connection:

```bash
<program> client <ip address>
```

## How Does It Work?

> [!NOTE]
> This is how it _should_ work, as the implementation is yet to be completed 😁

### Overview

The server centrally manages information amongst all the clients. A client will
send a message to the server, which then relays that message to all the clients.

### Protocol

The chatroom is governed by a simple application layer protocol. All data send
by the server and clients must adhere to this protocol. 

Each message is structured like so:

```
<ACTION> "<ARG1>" "<ARG2>" ...
```

The actions are all described by a single, leading byte.  The following actions 
are available:

- `0x00 (ACKNOWLEDGE)` - Simple acknowledgement of a message. Useful if no 
    response is required. Takes no arguments.
- `0x10 (LOGIN)` - Requests to join the chatroom. Takes a single argument of `<NAME>`.
- `0x11 (ACCEPT)` - Accepts a login request. No arguments.
- `0x12 (REJECT)` - Rejects a login request. No arguments.
- `0x13 (LOGOUT)` - Broadcasts that they are (gracefully) leaving the chatroom.
    No arguments.
- `0x20 (MESSAGE)` - Sends a new message to the users. Takes a single argument 
    of `<MESSAGE>`.