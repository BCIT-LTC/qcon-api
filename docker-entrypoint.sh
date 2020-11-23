>&2 echo "Run Database migrations"
python manage.py migrate

echo "-------------------------------------------------------------------------------------------\n"

#Start NGINX
# >&2 echo "Starting nginx..."
# nginx -g 'daemon off;'
# nginx

>&2 echo "create logging directory"
mkdir log


>&2 echo "Start Django Q task scheduler"
# python /code/manage.py qcluster &

echo "-------------------------------------------------------------------------------------------\n"


#Start django dev server
>&2 echo "Starting Django runserver..."
python manage.py runserver 0.0.0.0:8000

