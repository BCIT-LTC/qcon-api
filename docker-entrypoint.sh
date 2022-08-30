#!/bin/sh

# set secrets from Vault init container or from dev configmap
if [ -f "/vault/secrets/config" ]; then echo -e "$(cat /vault/secrets/config)" >> .env;
export $(grep -v '^#' .env | xargs -0); fi

>&2 echo "make Database migrations"
python manage.py makemigrations api_v2 api_v3
echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Run Database migrations"
python manage.py migrate
echo "-------------------------------------------------------------------------------------------\n"

#Collect static files
>&2 echo "Collect static"
python manage.py collectstatic --noinput

>&2 echo "Create superuser 'admin'"
echo "from django.contrib.auth.models import User; \
        User.objects.filter(username='$ADMIN_USERNAME').exists() or \
        User.objects.create_superuser('$ADMIN_USERNAME', 'admin@example.com', '$ADMIN_PASSWORD');" \
    | python /code/manage.py shell
echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Create API TOKEN"
echo "from api_v2.models import CustomToken; \
        from django.contrib.auth.models import User; \
        theuser = User.objects.get(username='$ADMIN_USERNAME'); \
        CustomToken.objects.filter(user=theuser).exists() or \
        CustomToken.objects.create(user=theuser, key='$API_KEY'); \
        print('API Token: ' + str(CustomToken.objects.get(user=theuser)))" \
    | python /code/manage.py shell
echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Starting redis"
redis-server --daemonize yes

>&2 echo "Starting Celery"
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker1@%h --detach
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker2@%h --detach
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker3@%h --detach
celery -A qcon worker --loglevel=INFO --concurrency=4 -n worker4@%h --detach

>&2 echo "Starting Supervisor"
exec "$@"
