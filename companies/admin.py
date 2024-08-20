from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'cif', 'city', 'is_active')
    search_fields = ('company_name', 'cif', 'city')
    list_filter = ('is_active', 'city')
    ordering = ('company_name',)
