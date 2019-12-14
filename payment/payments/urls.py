from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('payments/', views.PaymentsList.as_view(), name='index'),
    path('customers/', views.CustomersView.as_view(), name='customers'),
    path('billers/', views.BillersView.as_view(), name='billers'),
    path('newpayment/', views.NewPayment.as_view(), name='new_payment'),
    path('savepayment/', views.SavePayment.as_view(), name='save_payment'),
    path('newbiller/', views.NewBiller.as_view(), name='newbiller'),
    path('savebiller/', views.SaveBiller.as_view(), name='save_biller'),
]
