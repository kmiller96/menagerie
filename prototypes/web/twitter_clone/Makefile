venv .venv:
	rm -rf .venv
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt
.PHONY: .venv

dev:
	.venv/bin/fastapi dev