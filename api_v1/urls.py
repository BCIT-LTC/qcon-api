from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api', views.Upload.as_view()),
    # path('api/<int:session>', views.Download),
    # path('api/download', views.DownloadTest),
    path('media/<int:session>/<filename>', views.Download),
    path('api/cli', views.CliUpload.as_view(), name='cli'),
]