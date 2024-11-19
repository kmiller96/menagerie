docker build -t main . \
&& \
docker run \
    --rm \
    --network host \
    --privileged \
    -v /var/run/docker.sock:/var/run/docker.sock \
    main