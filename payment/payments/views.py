from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomersForm, BillersForm, NewCustomerForm, NewBillerForm
from .models import Payment, Customer, Biller


class PaymentsList(generic.ListView):
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

    # def get(self, request):
    #     latest_payments_list = Payment.objects.order_by('-pub_date')
    #     customers = CustomersForm()
    #     billers = BillersForm()
    #     context = {'customers': customers, 'billers': billers, 'latest_payments_list': latest_payments_list}
    #     template_name = 'payment/index.html'
    #     return render(request, template_name, context)


# def index(request):
#     latest_payments_list = Payment.objects.order_by('-pub_date')
#     context = {'latest_payments_list': latest_payments_list}
#     customers = CustomersForm()
#     billers = BillersForm()
#     filters = {'customers': customers, 'billers': billers}
#
#     filter_details = request.GET
#     customer_text = filter_details.get('choose_customer')
#     biller_text = filter_details.get('choose_biller')
#     template_path = 'payment/index.html'
#     if customer_text == 'None' and biller_text == 'None' or customer_text is None and biller_text is None:
#         return render(request, template_path, {**context, **filters})
#     elif customer_text == 'None' and biller_text != 'None':
#         latest_payments_list = Payment.objects.filter(biller__biller_text=biller_text).order_by('-pub_date')
#     elif customer_text != 'None' and biller_text == 'None':
#         latest_payments_list = Payment.objects.filter(customer__customer_text=customer_text).order_by('-pub_date')
#     else:
#         latest_payments_list = Payment.objects.filter(customer__customer_text=customer_text,
#                                                       biller__biller_text=biller_text).order_by('-pub_date')
#
#     return render(request, template_path,
#                   {'latest_payments_list': latest_payments_list, **filters})


class BillersView(generic.ListView):
    model = Biller
    template_name = 'payment/billers.html'
    context_object_name = 'latest_billers_list'


class CustomersView(generic.ListView):
    model = Customer
    template_name = 'payment/customers.html'
    context_object_name = 'latest_customers_list'


class NewPayment(generic.TemplateView):
    template_name = 'payment/newpayment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_customers_list'] = Customer.objects.order_by('customer_text')
        context['latest_billers_list'] = Biller.objects.order_by('biller_text')
        return context


class NewBiller(generic.View):
    def get(self, request):
        form = NewBillerForm()
        context = {'form': form}
        template_name = "payment/newbiller.html"
        return render(request, template_name, context)


class NewCustomer(generic.View):
    def get(self, request):
        form = NewCustomerForm()
        context = {'form': form}
        template_name = "payment/newcustomer.html"
        return render(request, template_name, context)


class SaveCustomer(generic.CreateView):
    model = Customer
    fields = ['customer_text']
    success_url = reverse_lazy('index')


class SaveBiller(generic.CreateView):
    model = Biller
    fields = ['biller_text']
    success_url = reverse_lazy('index')


class SavePayment(generic.CreateView):
    model = Payment
    fields = ['customer', 'biller', 'account', 'amount']
    success_url = reverse_lazy('index')

# def billers(request):
#     latest_billers_list = Biller.objects.order_by('biller_text')
#     context = {'latest_billers_list': latest_billers_list}
#     return render(request, 'payment/billers.html', context)

# def customers(request):
#     latest_customers_list = Customer.objects.order_by('customer_text')
#     context = {'latest_customers_list': latest_customers_list}
#     return render(request, 'payment/customers.html', context)

# def new_payment(request):
#     latest_customers_list = Customer.objects.order_by('customer_text')
#     latest_billers_list = Biller.objects.order_by('biller_text')
#     context = {'latest_customers_list': latest_customers_list,
#                'latest_billers_list': latest_billers_list}
#     return render(request, 'payment/newpayment.html', context)


# def new_biller(request):
#     add_biller = NewBillerForm()
#     template_name = "payment/newbiller.html"
#     return render(request, template_name, {'add_biller': add_biller})
#     return redirect('index')

# def new_customer(request):
#     add_customer = NewCustomerForm()
#     template_name = "payment/newcustomer.html"
#     return render(request, template_name, {'add_customer': add_customer})

# def save_customer(request):
#     customer_details = request.body.decode('utf-8').split('&')
#     customer_name = customer_details[1].split('=')[1]
#     Customer.objects.create_customer(customer_name)


# def save_biller(request):
#     biller_details = request.body.decode('utf-8').split('&')
#     biller_name = biller_details[1].split('=')[1]
#     Biller.objects.create_biller(biller_name)
#     return redirect('index')

# Create your views here.


# def save_payment(request):
#     payment_details = request.body.decode('utf-8').split('&')
#     customer_id = payment_details[1].split('=')[1]
#     biller_id = payment_details[2].split('=')[1]
#     account = payment_details[3].split('=')[1]
#     amount = payment_details[4].split('=')[1]
#     customer = Customer.objects.get(pk=customer_id)
#     biller = Biller.objects.get(pk=biller_id)
#     payment = Payment(customer=customer, biller=biller, account=account, amount=amount)
#     payment.save()
#     return redirect('index')
