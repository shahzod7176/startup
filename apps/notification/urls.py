from django.urls import path
from notification.views import NotificationListCreateView, NotificationUpdateView

urlpatterns = [
    path('notifications/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationUpdateView.as_view(), name='notification-update'),
]
