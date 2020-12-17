from django.urls import path, re_path
from django.conf.urls import url
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # path('media/<int:id>/<filename>', views.Download),
    path('api/cli', views.CliUpload.as_view(), name='cli'),

    path('api/status/<int:id>', views.GetStatus.as_view(), name='status'),
    path('api/upload', views.Upload.as_view(), name='upload'),
    path('api/setsection', views.SetSection.as_view(), name='setsection'),
    path('media/<int:id>/<filename>', views.Download.as_view()),
    path('api/download/<int:id>', views.DownloadAPI.as_view(), name='download'),
    # path('api/download', views.CliUpload.as_view(), name='download'),
    # path('api/execute', views.CliUpload.as_view(), name='execute'),
    # path('api/getmarkdown', views.CliUpload.as_view(), name='getmarkdown'),
    # path('api/getimsmanifest', views.CliUpload.as_view(), name='getimsmanifest'),
    # path('api/getquestiondb', views.CliUpload.as_view(), name='getquestiondb'),

    # OPENAPI
    # PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # UI:
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/doc2/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]