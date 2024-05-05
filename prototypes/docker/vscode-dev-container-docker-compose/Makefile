venv .venv:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

up:
	docker compose up --detach --build

down:
	docker compose down