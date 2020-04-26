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
