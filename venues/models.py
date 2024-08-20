from django.db import models
from companies.models import Company

class Venue(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='venues')
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()

    def __str__(self):
        return self.name
