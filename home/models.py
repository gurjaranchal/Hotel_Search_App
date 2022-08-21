from django.db import models
from pyrsistent import m

class Emenities(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Hotels(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_description=models.TextField()
    hotel_image=models.CharField(max_length=500)
    price=models.IntegerField()
    hotel_link=models.CharField(max_length=500)
    emenities=models.ManyToManyField(Emenities)
    

    def __str__(self):
        return self.hotel_name

# Create your models here.
