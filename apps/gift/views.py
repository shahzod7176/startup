from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from gift.models import GiftSent
from gift.serializers import GiftSentSerializer


@extend_schema(tags=['gift'])
class GiftSentListCreateAPIView(ListCreateAPIView):
    queryset = GiftSent.objects.all()
    serializer_class = GiftSentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GiftSent.objects.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
