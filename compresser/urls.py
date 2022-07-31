from django.urls import path
from . import views

app_name = "compressor"


urlpatterns = [
    path("", views.upload, name="upload"),
    path("compress/<int:pk>", views.CompressImageView.as_view(), name="compress"),
]