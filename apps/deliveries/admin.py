from django.contrib import admin
from django.contrib.admin import ModelAdmin

from deliveries.models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(ModelAdmin):
    list_display = ['courier', 'status', 'delivered_at', 'created_at']
    list_filter = ['status', 'created_at']
