from django.db import models
from adminapp.models import *
# Create your models here.

class Regdb(models.Model):
    regname = models.CharField(max_length=20)
    regpswd = models.CharField(max_length=20)
    regmail = models.EmailField()
    regadd = models.TextField(max_length=60)

class Condb(models.Model):
    contactmsg = models.TextField(max_length=100)
    contactname = models.CharField(max_length=20)
    contactmail = models.EmailField()

class Cartdb(models.Model):
    userid = models.ForeignKey(Regdb,on_delete= models.CASCADE)
    prdid = models.ForeignKey(Prdb,on_delete=models.CASCADE)
    cqty = models.IntegerField()
    ctot = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

class Checkout(models.Model):
    userid = models.ForeignKey(Regdb,on_delete=models.CASCADE)
    cartid = models.ForeignKey(Cartdb,on_delete=models.CASCADE,null=True)
    address = models.TextField(max_length=60)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    postalcode = models.CharField(max_length=20)
    mobile = models.IntegerField()
    mail = models.EmailField(default='null')

