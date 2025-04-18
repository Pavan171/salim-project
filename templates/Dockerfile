FROM python:3.10-slim

RUN apt-get update && apt-get install -y netcat-openbsd gcc libpq-dev && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x wait_for_postgres.sh

CMD ["./wait_for_postgres.sh"]
