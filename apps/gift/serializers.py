from rest_framework.serializers import ModelSerializer

from gift.models import GiftSent


class GiftSentSerializer(ModelSerializer):
    class Meta:
        model = GiftSent
        fields = ['id', 'sender', 'receiver', 'gift_description', 'provide', 'delivery_date', 'status']
        read_only_fields = ['id', 'sender', 'receiver', 'delivery_date', 'gift_description']
