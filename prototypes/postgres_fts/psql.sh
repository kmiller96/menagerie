ARGS=${@}

docker run \
    -it --rm --network host \
    postgres:14 \
    psql \
    --host localhost \
    --port 5432 \
    --username postgres \
    postgres ${ARGS}