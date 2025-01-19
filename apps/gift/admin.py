from django.contrib.admin import ModelAdmin
from django.contrib import admin

from gift.models import GiftSent


@admin.register(GiftSent)
class GiftSentAdmin(ModelAdmin):
    list_display = ['sender', 'receiver', 'gift_description', 'provide', 'delivery_date', 'status']
    search_fields = ('gift_description',)
    list_filter = ('sender', 'receiver')
