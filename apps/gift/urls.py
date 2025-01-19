from django.urls import path

from gift.views import GiftSentCreateView

urlpatterns = [
    path('create/', GiftSentCreateView.as_view(), name='create_gift_sent'),
]
