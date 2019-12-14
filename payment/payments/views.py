from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomersForm, BillersForm, NewBillerForm
from .models import Payment, Customer, Biller


class PaymentsList(LoginRequiredMixin, generic.ListView):
    model = Payment
    template_name = 'payment/index.html'
    context_object_name = 'latest_payments_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = CustomersForm
        context['billers'] = BillersForm
        return context

    def get_queryset(self, *args, **kwargs):
        filter_details = self.request.GET
        customer = filter_details.get('choose_customer')
        biller = filter_details.get('choose_biller')
        if customer == 'None' and biller == 'None' or customer is None and biller is None:
            return Payment.objects.order_by('-pub_date')
        elif customer == 'None' and biller != 'None':
            return Payment.objects.filter(biller__biller_text=biller).order_by('-pub_date')
        elif customer != 'None' and biller == 'None':
            return Payment.objects.filter(customer__customer_text=customer).order_by('-pub_date')
        else:
            return Payment.objects.filter(customer__customer_text=customer,
                                          biller__biller_text=biller).order_by('-pub_date')


class BillersView(LoginRequiredMixin, generic.ListView):
    model = Biller
    template_name = 'payment/billers.html'
    context_object_name = 'latest_billers_list'


class CustomersView(LoginRequiredMixin, generic.ListView):
    model = Customer
    template_name = 'payment/customers.html'
    context_object_name = 'latest_customers_list'


class NewPayment(LoginRequiredMixin, generic.TemplateView):
    template_name = 'payment/newpayment.html'

    def get_context_data(self, **kwargs):
        username = self.request.user
        context = super().get_context_data(**kwargs)
        context['latest_customers_list'] = Customer.objects.filter(customer_text=username)
        context['latest_billers_list'] = Biller.objects.order_by('biller_text')
        return context


class NewBiller(LoginRequiredMixin, generic.View):
    def get(self, request):
        form = NewBillerForm()
        context = {'form': form}
        template_name = "payment/newbiller.html"
        return render(request, template_name, context)


class SaveBiller(LoginRequiredMixin, generic.CreateView):
    model = Biller
    fields = ['biller_text']
    success_url = reverse_lazy('index')


class SavePayment(LoginRequiredMixin, generic.CreateView):
    model = Payment
    fields = ['customer', 'biller', 'account', 'amount']
    success_url = reverse_lazy('index')
