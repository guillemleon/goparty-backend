from django.db import models
from companies.models import Company
from venues.models import Venue

class Event(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=255)
    description_title = models.CharField(max_length=255)
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=255)
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
