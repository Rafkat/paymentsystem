from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from authentication.forms import NewUser
from authentication.models import DUser


class Registration(generic.View):
    def get(self, request):
        template_name = 'registration/registration.html'
        form = NewUser()
        context = {'form': form}
        return render(request, template_name, context)


class SaveUser(generic.CreateView):
    model = DUser
    fields = ['username', 'password']
    success_url = '/payments/'

# Create your views here.
