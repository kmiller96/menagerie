venv .venv:
	rm -rf .venv
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

dev:
	.venv/bin/fastapi dev

server:
	.venv/bin/fastapi run