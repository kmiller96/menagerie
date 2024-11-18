IMAGE_NAME = stdin-demo

venv .venv:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

image:
	docker build -t $(IMAGE_NAME) .

run:
	echo 'run me!' | docker run -i --rm $(IMAGE_NAME) 

cleanup:
	docker rmi $(IMAGE_NAME)