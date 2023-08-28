from django.db import models
# Create your models here.

class Pipes(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.DecimalField(decimal_places=4,max_digits=8)
    rate=models.DecimalField(decimal_places=4,max_digits=8)
    def __str__(self):
        return self.brand


class Cables(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.DecimalField(decimal_places=4,max_digits=8)
    rate=models.DecimalField(decimal_places=4,max_digits=8)
    def __str__(self):
        return self.brand

class SwitchGear(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.DecimalField(decimal_places=4,max_digits=8)
    rate=models.DecimalField(decimal_places=4,max_digits=8)
    def __str__(self):
        return self.brand

class Electricals(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.DecimalField(decimal_places=4,max_digits=8)
    rate=models.DecimalField(decimal_places=4,max_digits=8)
    def __str__(self):
        return self.brand

class Accessories(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.DecimalField(decimal_places=4,max_digits=8)
    rate=models.DecimalField(decimal_places=4,max_digits=8)
    def __str__(self):
        return self.brand


class FRPPoleBox(models.Model):
    brand=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    size=models.DecimalField(decimal_places=4,max_digits=8)
    rate=models.DecimalField(decimal_places=4,max_digits=8)
    def __str__(self):
        return self.brand