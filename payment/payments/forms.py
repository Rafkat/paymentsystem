from django import forms
from .models import Customer, Biller


class Customers(forms.Form):
    customer = str(Customer.objects.order_by('customer_text'))
    latest_customers_list = forms.Select(choices=[(customer, str(Customer.objects.order_by('customer_text')))])



class Billers(forms.Form):
    biller = str(Biller.objects.order_by('biller_text'))
    latest_biller_list = forms.ChoiceField(choices=[(biller, Biller.objects.order_by('biller_text'))])
