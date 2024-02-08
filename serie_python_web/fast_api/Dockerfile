FROM python:3.9

WORKDIR /app

RUN pip install --only-binary :all: fastapi[all]

COPY . .

CMD cd /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]