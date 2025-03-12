#!/bin/sh
set -e

echo "Running database migrations..."
python manage.py migrate

echo "Starting server..."
exec "$@" # Executes the command from Dockerfile CMD or docker-compose command