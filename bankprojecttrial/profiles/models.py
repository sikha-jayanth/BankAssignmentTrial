from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    Place = models.CharField(max_length=100, default='')
    address = models.TextField()
    def __str__(self):
        return self.user





class AccountInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='map')
    account_no = models.CharField(max_length=10, unique=True)
    balance = models.IntegerField(default=1000)
    account_pin = models.IntegerField(unique=True)
    date_opened = models.DateField(default=datetime.today())

    def __str__(self):
        return self.account_no


class Transactions(models.Model):
    account_no=models.ForeignKey(AccountInfo,on_delete=models.CASCADE)
    account_pin=models.IntegerField()
    amount=models.IntegerField(default=100)
    choices = (
        ("deposit", "deposit"), ("withdraw", "withdraw")
    )
    type=models.CharField(max_length=100, choices=choices, default="deposit")
    transaction_date_time = models.DateField("date and time", default=datetime.now())


class Transfer(models.Model):
    from_account=models.CharField(max_length=100)
    to_account=models.ForeignKey(AccountInfo,on_delete=models.CASCADE)
    amount=models.IntegerField(default=100)
    account_pin=models.IntegerField()
    transfer_date_time=models.TimeField("date and time",default=datetime.now())
