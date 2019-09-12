from django.db import models
from django.utils import timezone

import datetime

class Payment(models.Model):
    payment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.payment_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Customer(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE,
                                    primary_key=True)
    customer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_text

class Biller(models.Model):
    payment = models.ForeignKey(Payment,
                                on_delete=models.CASCADE)
    biller_text = models.CharField(max_length=200)

    def __str__(self):
        return self.biller_text

class Amount(models.Model):
    payment = models.OneToOneField(Payment,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    amount_value = models.FloatField(max_length=200)

    def __str__(self):
        return self.amount_value

# Create your models here.
