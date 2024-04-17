# url_shortener/urls.py

from django.urls import path
from .views import home, redirect_original 

urlpatterns = [
    path('', home, name='home'),
    path('<str:short_url>/', redirect_original, name='redirect_original'),
]
