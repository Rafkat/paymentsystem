from django.db import models
from django.utils import timezone

import datetime


class NewBC(models.Manager):
    def create_customer(self, customer_text):
        newcustomer = self.create(customer_text=customer_text)
        return newcustomer

    def create_biller(self, biller_text):
        newbiller = self.create(biller_text=biller_text)
        return newbiller


class Customer(models.Model):
    customer_text = models.CharField(max_length=200)

    objects = NewBC()

    def __str__(self):
        return self.customer_text


class Biller(models.Model):
    biller_text = models.CharField(max_length=200)

    objects = NewBC()

    def __str__(self):
        return self.biller_text


class Payment(models.Model):
    payment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True, null=True)
    amount = models.FloatField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    biller = models.ForeignKey(Biller, on_delete=models.CASCADE, null=True)
    account = models.IntegerField(null=True)

    def __str__(self):
        return self.amount

    def __str__(self):
        return self.payment_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



# Create your models here.
