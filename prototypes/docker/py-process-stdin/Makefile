IMAGE_NAME = stdin-demo

venv .venv:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

images:
	docker build -t tap-mock ./tap_mock/
	docker build -t target-csv ./target_csv/

tap_mock:
	@docker run --rm tap-mock
.PHONY: tap_mock

target_csv:
	@docker run --rm --volume ./output:/app --workdir /app --interactive target-csv
.PHONY: target_csv

demo:
	bash demo.sh

cleanup:
	docker rmi tap-mock || true
	docker rmi target-csv || true
	docker rmi read-stdin || true