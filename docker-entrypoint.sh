#!/bin/sh
set -e

>&2 echo "make Database migrations"
python manage.py makemigrations api_v2
echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Run Database migrations"
python manage.py migrate
echo "-------------------------------------------------------------------------------------------\n"

#Start NGINX
# >&2 echo "Starting nginx..."
# nginx -g 'daemon off;'
# nginx

#Collect static files
>&2 echo "Collect static"
python manage.py collectstatic

# >&2 echo "Start Django Q task scheduler"
# python manage.py qcluster &
# echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Create temporary superuser"
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python /code/manage.py shell
echo "-------------------------------------------------------------------------------------------\n"

#Start django dev server
>&2 echo "Starting Gunicorn"
gunicorn --bind 0.0.0.0:8001 qcon.wsgi --daemon

>&2 echo "Starting Nginx"
exec "$@"