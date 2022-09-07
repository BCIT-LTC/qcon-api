#!/usr/bin/env sh

set -e

# set secrets from Vault init container or from dev configmap
if [ -f "/vault/secrets/config" ]; then echo "$(cat /vault/secrets/config)" >> .env; fi

>&2 echo "make Database migrations"
python manage.py makemigrations api_v3
echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Run Database migrations"
python manage.py migrate
echo "-------------------------------------------------------------------------------------------\n"

#Collect static files
>&2 echo "Collect static"
python manage.py collectstatic --noinput

>&2 echo "Starting redis"
redis-server --daemonize yes

>&2 echo "Starting Celery"
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker1@%h --detach
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker2@%h --detach
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker3@%h --detach
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker4@%h --detach

>&2 echo "Starting Supervisor"
exec "$@"
