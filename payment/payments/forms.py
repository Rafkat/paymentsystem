from django import forms
from .models import Customer, Biller


class CustomersForm(forms.Form):
    customers_list = Customer.objects.all()
    Choose_customer = forms.ChoiceField(choices=[(customer, customer) for customer in customers_list])


class BillersForm(forms.Form):
    billers_list = Biller.objects.all()
    Choose_biller = forms.ChoiceField(choices=[(biller, biller) for biller in billers_list])
