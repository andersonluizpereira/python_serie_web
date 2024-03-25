FROM python:3.9

WORKDIR /app

RUN pip install --only-binary :all: fastapi[all], pybreaker

COPY . .

CMD cd /app
FROM redis
COPY redis.conf /usr/local/etc/redis/redis.conf

CMD ["redis-server", "/usr/local/etc/redis/redis.conf" ]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]