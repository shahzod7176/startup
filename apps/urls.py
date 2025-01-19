from django.urls import include, path

urlpatterns = [
    path('gift/', include('gift.urls')),
    path('profiles/', include('profiles.urls')),
    path('notification/', include('notification.urls')),
    path('deliveries/', include('deliveries.urls')),
    path('authentication/', include('authentication.urls'))
]
