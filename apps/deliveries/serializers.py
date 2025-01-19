from rest_framework.serializers import ModelSerializer

from deliveries.models import Delivery


class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'courier', 'address', 'status', 'delivered_at', 'created_at']
        read_only_fields = ['id', 'created_at']
