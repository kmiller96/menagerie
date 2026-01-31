import socket

PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to all interfaces so we receive broadcast packets
sock.bind(("", PORT))

print(f"Listening for UDP broadcasts on port {PORT}")

while True:
    data, addr = sock.recvfrom(4096)
    print(f"Received from {addr}: {data!r}")
