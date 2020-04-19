from django.db import models

# Create your models here.

class Cooperative(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField
    phone2 = models.IntegerField
    fax = models.CharField(max_length=50)
    mail = models.EmailField(max_length=200)


class Travel(models.Model):
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    origin = models.ForeignKey(City, on_delete=models.CASCADE)
    route = models.CharField(max_length=200)
    destination = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isactive = models.BooleanField 


class City(models.Model):
    name = models.CharField(max_length=50)


class Schedule(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    hout = models.DateTimeField