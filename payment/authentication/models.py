from django.db import models
from django.contrib.auth.models import User

from payments.models import Customer


class NUser(models.Manager):
    def create_user(self, username, email):
        new_user = self.create(username=username, email=email)
        return new_user


class DUser(User):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)
    objects = NUser()

    def __str__(self):
        return self.user

# Create your models here.
