from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Payment, Customer, Biller

def index(request):
    latest_payments_list = Payment.objects.order_by('-pub_date')[:5]
    context = {'latest_payments_list': latest_payments_list}
    return render(request, 'payment/index.html', context)

def customers(request):
    return HttpResponse("You're looking at customer")


def billers(request):
    return HttpResponse("You're looking at biller")

def new_payment(request):
    return HttpResponse("You're looking at new payment")




# Create your views here.
