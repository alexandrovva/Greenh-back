from django.db import models
    
class Flower(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=255)
    light = models.TextField()
    temp = models.TextField()
    humidity = models.TextField()
    watering = models.TextField()
    fertilizer = models.TextField()
    transplantatio = models.TextField()

class Shipping(models.Model):
    name = models.CharField(max_length=55)
    phone = models.CharField(max_length=55)
    flower = models.ForeignKey(Flower, blank=True, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    name = models.CharField(max_length=55)
    text = models.TextField()
    flower = models.ForeignKey(Flower, blank=True, on_delete=models.CASCADE, null=True)

class Manager(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    