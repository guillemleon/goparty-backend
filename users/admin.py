from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import User, UserCustomer, UserCompany


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        'email',
    ]
    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'password1',
                'password2',
            ),
        })
    ),
    ordering = []
    list_filter = []
    filter_horizontal = []
    readonly_fields = []


@admin.register(UserCustomer)
class UserCustomerAdmin(BaseUserAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'phone',
        'type',
        'is_active',
        'accepted_terms'
    ]
    fieldsets = (
        (None, {'fields': ('password', 'accepted_terms',)}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'email', 'phone', 'avatar',)}),
        (_('Readonly fields'), {
            'fields': (
                'type',
            )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
    readonly_fields = ['type']
    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'phone',
                'password1',
                'password2',
            ),
        })
    ),
    ordering = []
    list_filter = []
    filter_horizontal = []


@admin.register(UserCompany)
class UserCompanyAdmin(BaseUserAdmin):
    list_display = [
        'email',
        'company_name',
        'phone',
        'cif',
        'type',
        'is_active',
        'accepted_terms'
    ]
    fieldsets = (
        (None, {'fields': ('password', 'accepted_terms',)}),
        (_('Personal info'), {
         'fields': (
             'company_name',
             'cif',
             'email',
             'phone',
             'country',
             'city',
             'address',
             'description',
             'avatar',
         )}),
        (_('Readonly fields'), {
            'fields': (
                'type',
            )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
    readonly_fields = ['type']
    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'company_name',
                'cif',
                'password1',
                'password2',
            ),
        })
    ),
    ordering = []
    list_filter = []
    filter_horizontal = []
