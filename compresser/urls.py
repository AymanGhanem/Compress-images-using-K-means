from django.urls import path
from . import views

app_name = "compressor"


urlpatterns = [
    path("", views.upload, name="upload"),
]