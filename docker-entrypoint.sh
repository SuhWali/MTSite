#!/bin/sh
set -e

echo "Running database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec "$@" # Executes the command from Dockerfile CMD or docker-compose command