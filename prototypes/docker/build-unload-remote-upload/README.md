# Build, Unload, & Remote Upload

Simulation of how you can keep your build within a CI server and only push the
_built_ artifact to the remote.

This demo doesn't have a "remove". So, instead, it simulates this by deleting
the image and then loading it back in before running it.

Additionally, we are testing this with docker compose as this is a design that I
am using elsewhere.

## TL;DR

To run the full, working demo:

```bash
make
```

To show what would happen in the remote if the image didn't exist:

```bash
make down  # Ensure all containers are stopped
make rm    # Ensure all images are removed
make up    # This will fail becuase there is no image!
```
