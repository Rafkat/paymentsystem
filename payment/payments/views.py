from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Payment, Customer, Biller

def index(request):
    latest_payments_list = Payment.objects.order_by('-pub_date')[:10]
    context = {'latest_payments_list': latest_payments_list}
    return render(request, 'payment/index.html', context)

def customers(request):
    latest_customers_list = Customer.objects.order_by('customer_text')
    context = {'latest_customers_list': latest_customers_list}
    return render(request, 'payment/customers.html', context)


def billers(request):
    latest_billers_list = Biller.objects.order_by('biller_text')
    context = {'latest_billers_list': latest_billers_list}
    return render(request, 'payment/billers.html', context)


def new_payment(request):
    latest_customers_list = Customer.objects.order_by('customer_text')
    latest_billers_list = Biller.objects.order_by('biller_text')
    context = {'latest_customers_list': latest_customers_list,
               'latest_billers_list': latest_billers_list}
    return render(request, 'payment/newpayment.html', context)




# Create your views here.
