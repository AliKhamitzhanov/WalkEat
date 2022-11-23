from django.urls import path
from reg.views import RegisterView, LoginAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register")

]