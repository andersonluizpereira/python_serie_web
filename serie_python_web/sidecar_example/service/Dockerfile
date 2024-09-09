FROM python:3.9-slim

WORKDIR /app

RUN pip install --only-binary :all: fastapi[all]

COPY . /app

CMD ["python", "main.py"]