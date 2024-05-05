FROM python:slim

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY app.py /app/app.py

ENTRYPOINT [ "fastapi", "run", "--port", "80" ]