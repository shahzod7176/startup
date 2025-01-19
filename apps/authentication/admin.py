from django.contrib import admin
from authentication.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_email_verified', 'is_staff')
    search_fields = ('username', 'email')
