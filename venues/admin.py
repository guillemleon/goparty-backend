from django.contrib import admin
from .models import Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'latitude', 'longitude', 'address')
    search_fields = ('name', 'company__company_name', 'address')
    list_filter = ('company',)