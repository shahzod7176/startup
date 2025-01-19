from django.contrib import admin
from django.contrib.admin import ModelAdmin

from notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ['user', 'title', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['user__username', 'title']
