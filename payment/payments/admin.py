from django.contrib import admin

from .models import Payment, Customer, Biller, Amount

admin.site.register(Payment)
admin.site.register(Customer)
admin.site.register(Biller)
admin.site.register(Amount)




# Register your models here.
