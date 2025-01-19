from django.urls import path
from deliveries.views import DeliveryListCreateView, DeliveryUpdateView

urlpatterns = [
    path('deliveries/', DeliveryListCreateView.as_view(), name='delivery-list-create'),
    path('deliveries/<int:pk>/', DeliveryUpdateView.as_view(), name='delivery-update'),
]
