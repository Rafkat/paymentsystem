from django.db import models
from django.utils import timezone

import datetime

class Customer(models.Model):
    customer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_text

class Biller(models.Model):
    biller_text = models.CharField(max_length=200)

    def __str__(self):
        return self.biller_text


class Payment(models.Model):
    payment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    amount = models.FloatField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    biller = models.ForeignKey(Biller, on_delete=models.CASCADE, null=True)
    account = models.IntegerField(null=True)

    def __str__(self):
        return self.amount_value
    def __str__(self):
        return self.payment_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)






# Create your models here.
