from django.urls import path, re_path
from django.conf.urls import url
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # path('api', views.Upload.as_view()),
    # path('api/<int:session>', views.Download),
    # path('api/download', views.DownloadTest),
    path('media/<int:session>/<filename>', views.Download),
    path('api/cli', views.CliUpload.as_view(), name='cli'),
    path('api/status', views.GetStatus.as_view(), name='status'),
    
    # OPENAPI
    # PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # UI:
    path('api/doc1/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/doc2/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]