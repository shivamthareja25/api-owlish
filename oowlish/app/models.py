from django.db import models

class Customer(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    sale_amount = models.IntegerField(blank=True, null=True)
    lattitude = models.FloatField(max_length=20, blank=True, null=True)
    longitude = models.FloatField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)