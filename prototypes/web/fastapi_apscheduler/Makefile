venv .venv:
	rm -rf .venv
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

server app api: .venv
	.venv/bin/fastapi dev --port 8000