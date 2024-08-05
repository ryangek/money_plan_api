# example/urls.py
from django.urls import path

from example.views import index

urlpatterns = [
    path('apple-app-site-association', index),
]