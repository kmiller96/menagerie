rm -rf output/
mkdir output

docker run \
    --rm \
    tap-mock \
| \
docker run \
    --rm \
    --volume ./output:/app \
    --workdir /app \
    --interactive \
    target-csv \
> output/state.json