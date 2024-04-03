venv: .venv
.venv:
	rm -rf .venv
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt
.PHONY: .venv


serve:
	uvicorn server:app --reload