run:
	docker run \
		--rm \
		-it \
		--network host \
		-v ${PWD}/.caddy/data:/data \
		-v ${PWD}/.caddy/config:/config \
		-v ${PWD}/conf:/etc/caddy \
		-w /conf \
		caddy:latest