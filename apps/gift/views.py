from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from gift.models import GiftSent
from gift.serializers import GiftSentSerializer

@extend_schema(tags=['gift'])

class GiftSentCreateView(CreateAPIView):
    queryset = GiftSent.objects.all()
    serializer_class = GiftSentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
