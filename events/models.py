import os
from django.db import models
from users.models import UserCompany

# Create your models here.


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('images/', filename)


class Event(models.Model):
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    event_name = models.CharField(blank=False, max_length=100)
    event_image = models.ImageField(upload_to=get_file_path, blank=True)
    event_country = models.CharField(blank=False, max_length=100)
    event_city = models.CharField(blank=False, max_length=100)
    event_company_name = models.CharField(blank=True, max_length=300)
    event_date = models.DateTimeField(blank=False)
    event_hour = models.TimeField(blank=False)
    event_description = models.TextField(blank=False, max_length=500)
    event_company = models.ForeignKey(UserCompany, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.event_company:
            self.event_company_name = self.event_company.company_name
            self.event_country = self.event_company.country
            self.event_city = self.event_company.city
        super().save(*args, **kwargs)
