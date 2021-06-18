from django.urls import path, re_path
from django.conf.urls import url
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # path('media/<int:id>/<filename>', views.Download),

    # path('status/<int:id>', views.GetStatus.as_view(), name='status'),
    # path('result/<int:id>', views.GetResult.as_view(), name='result'),
    # path('upload', views.Upload.as_view(), name='upload'),
    path('wordzip', views.WordToZip.as_view(), name='WordToZip'),
    path('wordjson', views.WordToJson.as_view(), name='WordToJson'),
    path('wordjsonzip', views.WordToJsonZip.as_view(), name='WordToJsonZip'),
    # path('setsection', views.SetSection.as_view(), name='setsection'),
    # path('media/<int:id>/<filename>', views.Download.as_view()),
    # path('download/<int:id>', views.DownloadAPI.as_view(), name='download'),
    # path('api/download', views.CliUpload.as_view(), name='download'),
    # path('api/execute', views.CliUpload.as_view(), name='execute'),
    # path('api/getmarkdown', views.CliUpload.as_view(), name='getmarkdown'),
    # path('api/getimsmanifest', views.CliUpload.as_view(), name='getimsmanifest'),
    # path('api/getquestiondb', views.CliUpload.as_view(), name='getquestiondb'),

    # OPENAPI
    # PATTERNS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # UI:
    path('',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    # path('api/doc2/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]