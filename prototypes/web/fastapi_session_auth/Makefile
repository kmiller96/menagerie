VENV_ACTIVATE = . .venv/bin/activate

venv .venv:
	python3 -m venv .venv
	$(VENV_ACTIVATE); pip install -r requirements.txt
.PHONY: venv .venv	


dev:
	$(VENV_ACTIVATE); fastapi dev --reload src/

serve:
	$(VENV_ACTIVATE); fastapi run main:app 