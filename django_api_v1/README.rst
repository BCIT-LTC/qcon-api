=====
QCON API_V1
=====

Quick start
-----------

1. Add "api_v1" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'api_v1',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('api_v1/', include('api_v1.urls')),

3. Run ``python manage.py migrate`` to create the api_v1 models.

4. Start the development server and visit http://127.0.0.1:8000/api

5. Visit http://127.0.0.1:8000/admin/ for the admin interface