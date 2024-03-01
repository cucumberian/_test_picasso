from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("upload/", views.FileUploadView.as_view(), name="upload"),
    path("files/", views.FileListView.as_view(), name="files"),
    path("", views.HealthCheckView.as_view(), name="health_check"),
]
