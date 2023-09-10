from django.db import models
# Create your models here.

class Pipes(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    def __str__(self):
        return self.brand


class Cables(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    def __str__(self):
        return self.brand

class SwitchGear(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    def __str__(self):
        return self.brand

class Electricals(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    def __str__(self):
        return self.brand

class Accessories(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    def __str__(self):
        return self.brand


class FRPPoleBox(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    def __str__(self):
        return self.brand
    

class Review(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=50)
    product=models.CharField(max_length=100)
    review=models.CharField(max_length=250)
    date=models.DateField()
    rating=models.FloatField()
    def __str__(self):
        return self.name