from django.contrib import admin
from django.contrib.admin import ModelAdmin

from profiles.models import CustomerProfile



@admin.register(CustomerProfile)
class CustomerProfileAdmin(ModelAdmin):
    list_display = ['id', 'user', 'address', 'phone_number', 'additional_info', 'created_at', 'updated_at']

