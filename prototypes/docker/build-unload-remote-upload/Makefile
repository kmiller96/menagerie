demo: down build save rm load up

build:
	@echo "Building echoer image..."
	docker compose build

save:
	@echo "Saving echoer image..."
	docker image save \
		--output echoer.tar.gz \
		echoer
	
rm:
	@echo "Deleting echoer image..."
	docker image rm echoer

load:
	@echo "Loading echoer image..."
	docker image load \
		--input echoer.tar.gz

up:
	@echo "Starting echoer container..."
	docker compose up \
		--no-build \
		--pull never

down:
	@echo "Removing echoer container..."
	docker compose down