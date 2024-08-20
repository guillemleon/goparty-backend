from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    cif = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name
