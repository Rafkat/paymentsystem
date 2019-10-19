from django.urls import path

from . import views

urlpatterns = [
    # path('payments/', views.index, name='index'),
    path('payments/', views.PaymentsList.as_view(), name='index'),
    # path('customers/', views.customers, name='customers'),
    path('customers/', views.CustomersView.as_view(), name='customers'),
    # path('billers/', views.billers, name='billers'),
    path('billers/', views.BillersView.as_view(), name='billers'),
    # path('newpayment/', views.new_payment, name='new_payment'),
    path('newpayment/', views.NewPayment.as_view(), name='new_payment'),
    # path('savepayment/', views.save_payment, name='save_payment'),
    path('savepayment/', views.SavePayment.as_view(), name='save_payment'),
    # path('newbiller/', views.new_biller, name='newbiller'),
    path('newbiller/', views.NewBiller.as_view(), name='newbiller'),
    path('savecustomer/', views.SaveCustomer.as_view(), name='save_customer'),
    path('newcustomer/', views.NewCustomer.as_view(), name='newcustomer'),
    # path('newcustomer/', views.new_customer, name='newcustomer'),
    path('savebiller/', views.SaveBiller.as_view(), name='save_biller'),
]
