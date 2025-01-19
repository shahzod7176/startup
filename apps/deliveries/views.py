from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from deliveries.models import Delivery
from deliveries.serializers import DeliverySerializer

@extend_schema(tags=['Deliveries'])
class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Delivery.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

@extend_schema(tags=['Deliveries'])
class DeliveryUpdateView(generics.UpdateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Delivery.objects.all()
        return Delivery.objects.filter(courier=self.request.user)
