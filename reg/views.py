from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializator import (
    LoginSerializer,
    EmailVerificationSerializer,
    RegisterSerializer,
    ProfileSerializer,
    ChangePasswordSerializer
)
from rest_framework.decorators import APIView
from drf_yasg import openapi

from rest_framework_simplejwt.authentication import JWTAuthentication





class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer
    # renderer_classes = (UserRenderer)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data["email"])
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        "token",
        in_=openapi.IN_QUERY,
        description="Description",
        type=openapi.TYPE_STRING,
    )



class LoginAPIView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data["phone"]
                password = serializer.data["password"]
                user = authenticate(username=username, password=password)
                if user is None:
                    data = "User not found"
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST, data={"status": data}
                    )

                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)

                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "user": user.username,
                        "refresh": str(refresh),
                        "access": str(access),
                    }
                )
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return self.request.user
    

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)


        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)