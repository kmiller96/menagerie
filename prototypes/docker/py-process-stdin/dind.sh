docker build -t main . \
&& \
docker run \
    --rm \
    --privileged \
    -v /var/run/docker.sock:/var/run/docker.sock \
    main