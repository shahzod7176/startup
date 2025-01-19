# from drf_spectacular.utils import extend_schema
# from rest_framework import generics, status
# from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate
# from authentication.serializers import RegisterSerializer, LoginSerializer, UserSerializer
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# @extend_schema(tags=['authentication'])
# class RegisterView(CreateAPIView):
#     serializer_class = RegisterSerializer
#
#
# @extend_schema(tags=['authentication'])
# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(
#             username=serializer.validated_data['username'],
#             password=serializer.validated_data['password']
#         )
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#             })
#         return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#
#
# @extend_schema(tags=['authentication'])
# class UserProfileView(APIView):
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer
)

User = get_user_model()


@extend_schema(tags=['authentication'])
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


@extend_schema(tags=['authentication'])
class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = LoginSerializer(request.user)
        return Response(serializer.data)
    # serializer_class = LoginSerializer


@extend_schema(tags=['authentication'])
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
