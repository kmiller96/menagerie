"""Runs the same script as 'test.sh' but in Python."""

import docker


client = docker.from_env()


container = client.containers.run(
    "hello-world",
    detach=True,
)

container.wait()

stdout = container.logs(stdout=True, stderr=False)
stderr = container.logs(stdout=False, stderr=True)

container.remove()

print(stdout.decode())
