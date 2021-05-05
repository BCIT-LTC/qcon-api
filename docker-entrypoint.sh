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

# >&2 echo "Check if API_KEY set"
if [[ -z "${API_KEY}" ]];  
then  
echo "API_KEY is not set"  
exit 1
else  
echo "API_KEY found"
fi  

# >&2 echo "Check if ADMIN_USERNAME set"
if [[ -z "${ADMIN_USERNAME}" ]];  
then  
echo "ADMIN_USERNAME not set"  
exit 1
else  
echo ""
fi  

# >&2 echo "Check if ADMIN_PASSWORD set"
if [[ -z "${ADMIN_PASSWORD}" ]];  
then  
echo "ADMIN_PASSWORD not set"  
exit 1
else  
echo ""
fi  

# >&2 echo "Check if DEBUG set"
if [[ -z "${DEBUG}" ]];  
then  
echo "DEBUG not set. Continue in production mode"  
else  
echo ""
fi  

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

chmod -R 755 /var/lib/nginx


#Start django dev server
>&2 echo "Starting Gunicorn"
gunicorn --bind 0.0.0.0:8001 qcon.wsgi --daemon

>&2 echo "Starting Nginx"
exec "$@"