#!/bin/sh
set -e

# set env vars
source .env
export $(cut -d = -f 1 .env)
rm .env
# TODO: unset vars for running container

>&2 echo "make Database migrations"
python manage.py makemigrations api_v2
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

chmod -R 755 /var/lib/nginx

#Start gunicorn server
>&2 echo "Starting Gunicorn"
gunicorn --bind 0.0.0.0:8001 --timeout 240 qcon.wsgi --daemon
exec "$@"