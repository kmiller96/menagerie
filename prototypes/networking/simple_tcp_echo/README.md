# Simple TCP Echo

Implements a basic TCP server that simplies echos back the message it is sent.

If the server is started using `server.sh`, the messages will be written to
`messages.log` and the server logs will be printed to STDERR.

## Quickstart

```bash
bash server.sh  # Starts the server up. Blocking.
bash connect.sh <message>  # Connects to the server with telnet.
```