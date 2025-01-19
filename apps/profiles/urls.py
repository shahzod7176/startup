from django.urls import path
from profiles.views import CustomerProfileDetailView

urlpatterns = [
    path('profile/', CustomerProfileDetailView.as_view(), name='customer-profile-detail'),
]
