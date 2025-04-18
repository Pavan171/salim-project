#!/bin/sh

echo "⏳ Waiting for PostgreSQL to be available..."

while ! nc -z "$POSTGRES_HOST" 5432; do
  sleep 1
done

echo "✅ PostgreSQL is up! Starting Flask app..."
exec python app.py
