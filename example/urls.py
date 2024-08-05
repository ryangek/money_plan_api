# example/urls.py
from django.urls import path

from example.views import apple_app_site_association

urlpatterns = [
    path('', apple_app_site_association),
    path('apple-app-site-association', apple_app_site_association),
]