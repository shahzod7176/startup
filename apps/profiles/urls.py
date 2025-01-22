from django.urls import path
from profiles.views import CustomerProfileListCreateApiView

urlpatterns = [
    # path('profile/', CustomerProfileDetailView.as_view(), name='customer-profile-detail'),
    path('profile/', CustomerProfileListCreateApiView.as_view(), name='customer-profile-list'),
]
