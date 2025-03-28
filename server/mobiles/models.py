from django.db import models

# Create your models here.

class Mobile(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    display = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model}"
