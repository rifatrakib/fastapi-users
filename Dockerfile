FROM python:3.9-slim-buster

WORKDIR /api

COPY requirements.txt /api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
COPY ./server /api/server

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
