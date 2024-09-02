venv .venv:
	rm -rf .venv
	python3 -m venv .venv
	pip install -r requirements.txt

build:
	pip wheel script/v4/ -w dist/

deploy:
	scp -r dist/ root@xx.xx.xx.xx:/srv/app/