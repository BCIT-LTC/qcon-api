>&2 echo "Run Database migrations"
python manage.py migrate

echo "-------------------------------------------------------------------------------------------\n"

#Start NGINX
# >&2 echo "Starting nginx..."
# nginx -g 'daemon off;'
# nginx

>&2 echo "create logging directory"
mkdir log

#Start django dev server
>&2 echo "Starting Django runserver..."
python manage.py runserver 0.0.0.0:8000

