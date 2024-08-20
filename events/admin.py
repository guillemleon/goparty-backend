from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'date', 'city', 'is_active')
    search_fields = ('name', 'company__company_name', 'city')
    list_filter = ('date', 'city', 'company')
    ordering = ('-date',)

    def is_active(self, obj):
        return obj.company.is_active
    is_active.boolean = True
    is_active.short_description = 'Company Active'
