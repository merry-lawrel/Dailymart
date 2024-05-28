from django.db import models

# Create your models here.
class  Catdb(models.Model):
    categoryname = models.CharField(max_length=20)
    categorydesc = models.TextField(max_length=100)
    categoryimg = models.ImageField(upload_to='sample',default='null.jpg')

class Prdb(models.Model):
    productname = models.CharField(max_length=20)
    productcat = models.CharField(max_length=20)
    productimg = models.ImageField(upload_to='sample',default='null.jpg')
    productprc = models.IntegerField(default=0)