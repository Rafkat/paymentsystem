from django.urls import path

from payments.views import Billers, Customers, save_customer
from . import views

urlpatterns = [
    path('payments/', views.index, name='index'),
    # path('customers/', views.customers, name='customers'),
    path('customers/', Customers.as_view(), name='customers'),
    # path('billers/', views.billers, name='billers'),
    path('billers/', Billers.as_view(), name='billers'),
    path('newpayment/', views.new_payment, name='new_payment'),
    path('savepayment/', views.save_payment, name='save_payment'),
    path('newbiller/', views.new_biller, name='newbiller'),
    path('savecustomer/', views.save_customer, name='save_customer'),
    path('savecustomer/', save_customer.as_view(), name='save_customer'),
    path('newcustomer/', views.new_customer, name='newcustomer'),
    path('savebiller/', views.save_biller, name='save_biller'),
]
