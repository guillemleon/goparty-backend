from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'latitude', 'longitude', 'user_type', 'registration_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'user_type', 'registration_date', 'latitude', 'longitude')
    search_fields = ('email', 'first_name', 'last_name', 'user_type')
    ordering = ('email',)
