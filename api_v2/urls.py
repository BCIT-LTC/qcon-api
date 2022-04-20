# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.urls import include, path, re_path
from . import views
from django.conf import settings

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('wordzip', views.WordToZip.as_view(), name='WordToZip'),
    path('wordjson', views.WordToJson.as_view(), name='WordToJson'),
    path('wordjsonzip', views.WordToJsonZip.as_view(), name='WordToJsonZip'),

    # path('api/doc2/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # path('<str:namespace>/<str:name>/review/<slug:slug>', views.redirect_root),
    # path('<str:namespace>/<str:name>/review/<slug:slug>/<str:actualurl>', views.redirect_view)
    # path('<str:namespace>/<str:name>/review/<slug:slug>/', include([
    #     path('<str:actualurl>', views.redirect_view)
    # ]))
]