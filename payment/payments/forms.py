from django import forms
from .models import Customer, Biller


class CustomersForm(forms.Form):
    customers = Customer.objects.order_by('customer_text').all()
    none_list = [('None', 'None')]
    customers_list = [(customer, customer) for customer in customers]
    Choose_customer = forms.ChoiceField(choices=none_list+customers_list)


class BillersForm(forms.Form):
    billers = Biller.objects.order_by('biller_text').all()
    none_list = [('None', 'None')]
    billers_list = [(biller, biller) for biller in billers]
    Choose_biller = forms.ChoiceField(choices=none_list+billers_list)
