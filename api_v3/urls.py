# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.urls import include, path, re_path
from . import views
from django.conf import settings

urlpatterns = [
    # path('wordzip', views.WordToZip.as_view(), name='WordToZip'),
    path('convert', views.WordToJson.as_view(), name='WordToJson'),
    # path('wordjsonzip', views.WordToJsonZip.as_view(), name='WordToJsonZip'),
]
