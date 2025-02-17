from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.BigIntegerField()
    area = models.FloatField()
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name