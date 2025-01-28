from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, ListCreateAPIView
from notification.models import Notification
from notification.serializers import NotificationSerializer


@extend_schema(tags=['notification'])
class NotificationListCreateView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['notification'])
class NotificationUpdateView(UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
