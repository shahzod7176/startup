from rest_framework.serializers import ModelSerializer

from profiles.models import CustomerProfile


class CustomerProfileSerializer(ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['id', 'user', 'address', 'phone_number', 'additional_info', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
