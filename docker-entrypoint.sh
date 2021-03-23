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

# >&2 echo "Start Django Q task scheduler"
# python manage.py qcluster &
# echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Create superuser 'admin'"
echo "from django.contrib.auth.models import User; \
        User.objects.filter(username='admin').exists() or \
        User.objects.create_superuser('admin', 'admin@example.com', '$ADMIN_CREDENTIAL');" \
    | python /code/manage.py shell
echo "-------------------------------------------------------------------------------------------\n"


# >&2 echo "Create temporary API TOKEN"
# echo "from rest_framework.authtoken.models import Token; \
#         from django.contrib.auth.models import User; \
#         theuser = User.objects.get(username='admin'); \
#         token = Token.objects.create(user=theuser); \
#         print('API Token: ' + str(token))" \
#     | python /code/manage.py shell
# echo "-------------------------------------------------------------------------------------------\n"

>&2 echo "Create API TOKEN"
echo "from api_v2.models import CustomToken; \
        from django.contrib.auth.models import User; \
        theuser = User.objects.get(username='admin'); \
        token = CustomToken.objects.create(user=theuser, key='$API_KEY'); \
        print('API Token: ' + str(token))" \
    | python /code/manage.py shell
echo "-------------------------------------------------------------------------------------------\n"

# >&2 echo "Create temporary API TOKEN"
# python manage.py drf_create_token admin



#Start django dev server
>&2 echo "Starting Django runserver..."
exec "$@"