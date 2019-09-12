from django.urls import path
from . import views

urlpatterns = [
    path('', views.billers, name='billers'),
]