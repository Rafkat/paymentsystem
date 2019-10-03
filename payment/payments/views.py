from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import json
from django.views import generic

from .models import Payment, Customer, Biller


def index(request):
    latest_payments_list = Payment.objects.order_by('-pub_date')
    latest_customers_list = Customer.objects.order_by('customer_text')
    latest_billers_list = Biller.objects.order_by('biller_text')
    context = {'latest_payments_list': latest_payments_list}
    filters = {'latest_customers_list': latest_customers_list,
               'latest_billers_list': latest_billers_list}

    filter_details = request.GET
    customer_id = filter_details.get('customer_id')
    biller_id = filter_details.get('biller_id')
    template_path = 'payment/index.html'
    if customer_id is None and biller_id is None:
        return render(request, template_path, {**context, **filters})
    elif customer_id is None and biller_id is not None:
        latest_payments_list = Payment.objects.filter(biller_id=biller_id).order_by('-pub_date')
    elif biller_id is None and customer_id is not None:
        latest_payments_list = Payment.objects.filter(customer_id=customer_id).order_by('-pub_date')
    else:
        latest_payments_list = Payment.objects.filter(customer_id=customer_id,
                                                      biller_id=biller_id).order_by('-pub_date')

    return render(request, template_path, {'latest_payments_list': latest_payments_list, **filters})


# def customers(request):
#     latest_customers_list = Customer.objects.order_by('customer_text')
#     context = {'latest_customers_list': latest_customers_list}
#     return render(request, 'payment/customers.html', context)


# def billers(request):
#     latest_billers_list = Biller.objects.order_by('biller_text')
#     context = {'latest_billers_list': latest_billers_list}
# return render(request, 'payment/billers.html', context)


class billers(generic.ListView):
    template_name = 'payment/billers.html'
    context_object_name = 'latest_billers_list'
    model = Payment

    def get_queryset(self):
        return Biller.objects.order_by('biller_text')


class customers(generic.ListView):
    template_name = 'payment/customers.html'
    context_object_name = 'latest_customers_list'
    model = Payment

    def get_queryset(self):
        return Customer.objects.order_by('customer_text')


def new_payment(request):
    latest_customers_list = Customer.objects.order_by('customer_text')
    latest_billers_list = Biller.objects.order_by('biller_text')
    context = {'latest_customers_list': latest_customers_list,
               'latest_billers_list': latest_billers_list}
    return render(request, 'payment/newpayment.html', context)


def save_payment(request):
    payment_details = request.body.decode('utf-8').split('&')
    customer_id = payment_details[1].split('=')[1]
    biller_id = payment_details[2].split('=')[1]
    account = payment_details[3].split('=')[1]
    amount = payment_details[4].split('=')[1]
    customer = Customer.objects.get(pk=customer_id)
    biller = Biller.objects.get(pk=biller_id)
    payment = Payment(customer=customer, biller=biller, account=account, amount=amount)
    payment.save()
    return redirect('index')

# Create your views here.
