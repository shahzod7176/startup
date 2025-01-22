from django.urls import path

from gift.views import GiftSentListCreateAPIView

urlpatterns = [
    path('gift/', GiftSentListCreateAPIView.as_view(), name='create_gift_sent'),
]
