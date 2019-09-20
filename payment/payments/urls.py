from django.urls import path

from . import views

urlpatterns = [
    path('payments/', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('billers/', views.billers, name='billers'),
    path('newpayment/', views.new_payment, name='new_payment'),
]