from django.urls import path, include



urlpatterns = [
    path('violations/', include('violations.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='vio_guard'))
]
