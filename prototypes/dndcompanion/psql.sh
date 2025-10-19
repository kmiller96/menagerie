# Connects to the postgres database using psql

DATABASE_NAME=${1:-"default"}
EXTRA_ARGS=${2:-""}

docker run \
    -it --rm --network host \
    postgres:17 \
    psql \
    --host localhost \
    --port 5432 \
    --username admin \
    ${DATABASE_NAME} ${EXTRA_ARGS}