from django.contrib import admin
from events.models import Event
from django.utils.translation import gettext_lazy as _
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'event_name',
        'event_country',
        'event_city',
        'event_company_name',
        'event_date',
        'event_company',
    ]
    fieldsets = (
        (_('Event info'), {
         'fields': ('event_name', 'event_date', 'event_hour', 'event_description', 'event_image',)}),
        (_('Readonly fields'), {
            'fields': (
                'event_company',
                'event_company_name',
                'event_country',
                'event_city',
            )}),
    )
    readonly_fields = ['event_company_name', 'event_country', 'event_city']
    add_fieldsets = (
        (None, {
            'fields': (
                'event_name',
                'event_country',
                'event_city',
                'event_date',
                'event_hour',
                'event_description',
                'event_company',
            ),
        })
    ),
    ordering = ['event_date']
    list_filter = []
    filter_horizontal = []
