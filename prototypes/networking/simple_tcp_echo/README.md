# Simple TCP Echo

Implements a basic TCP server that simplies echos back the message it is sent.

If the server is started using `server.sh`, the messages will be written to
`messages.log` and the server logs will be printed to STDERR.

## Quickstart

```bash
bash server.sh  # Starts the server up. Blocking.
bash send.sh <message>  # Submits a TCP message to the server.
```