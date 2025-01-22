from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView

from profiles.models import CustomerProfile
from profiles.serializers import CustomerProfileSerializer

# @extend_schema(tags=['profiles'])
# class CustomerProfileDetailView(RetrieveUpdateAPIView):
#     queryset = CustomerProfile.objects.all()
#     serializer_class = CustomerProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_object(self):
#         return CustomerProfile.objects.get(sender=self.request.user)


@extend_schema(tags=['profiles'])
class CustomerProfileListCreateApiView(ListCreateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return CustomerProfile.objects.get(sender=self.request.user)

