venv .venv:
	rm -rf .venv
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
.PHONY: .venv

db:
	.venv/bin/python db.py	

server: db
	.venv/bin/fastapi dev