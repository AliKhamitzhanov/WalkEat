from django.urls import path, include

urlpatterns = [
    path('password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]