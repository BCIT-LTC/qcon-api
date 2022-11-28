# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""qcon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from api_v3 import views

urlpatterns = [
    # # path('admin/', admin.site.urls),
    path('', include('api_v3.urls')),
    # path('v2/', include('api_v2.urls')),
    path('v3/', include('api_v3.urls'))
]

if settings.DEBUG:
    # OPENAPI
    # PATTERNS
    # UI:
    urlpatterns += [
        path('v3/', include('api_v3.urls'))
    ]
else:
    urlpatterns += [path('', views.RootPath.as_view(), name='root')]

handler404 = 'api_v3.views.view_404'

if settings.ADMIN_ENABLED:
    urlpatterns += [path('admin/', admin.site.urls)]

# urlpatterns += staticfiles_urlpatterns()