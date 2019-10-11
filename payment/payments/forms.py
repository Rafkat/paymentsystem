from django import forms
from .models import Customer, Biller


class CustomersForm(forms.Form):
    customers = Customer.objects.order_by('customer_text').all()
    none_list = [('None', 'None')]
    customers_list = [(customer, customer) for customer in customers]
    choose_customer = forms.ChoiceField(choices=none_list + customers_list, label='Choose customer*:')


class BillersForm(forms.Form):
    billers = Biller.objects.order_by('biller_text').all()
    none_list = [('None', 'None')]
    billers_list = [(biller, biller) for biller in billers]
    choose_biller = forms.ChoiceField(choices=none_list + billers_list, label='Choose biller*:')


class NewCustomerForm(forms.Form):
    customer_text = forms.CharField(max_length=100, label='New customer*:')



