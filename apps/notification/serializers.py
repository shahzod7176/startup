from rest_framework.serializers import ModelSerializer

from notification.models import Notification


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'title', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
