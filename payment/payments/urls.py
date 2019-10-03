from django.urls import path

from payments.views import billers, customers
from . import views

urlpatterns = [
    path('payments/', views.index, name='index'),
    # path('customers/', views.customers, name='customers'),
    path('customers/', customers.as_view(), name='customers'),
    # path('billers/', views.billers, name='billers'),
    path('billers/', billers.as_view(), name='billers'),
    path('newpayment/', views.new_payment, name='new_payment'),
    path('savepayment/', views.save_payment, name='save_payment'),
]

