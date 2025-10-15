# TCP Phone Call

Emulates a phone call in raw TCP. Roughly what I'm envisioning.

- The server is "listening" for phone calls
- Client "dials".
- Server is alerted and accepts simple y/n answer prompt.
- Connects phones
- Each line can send and receive traffic.

Extensions:
- Can we add a timeout to the dialler, in case their friend doesn't pickup?

Better still if we can make it one program, compile it, and run the compiled
binary!
