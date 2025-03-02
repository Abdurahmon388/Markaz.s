from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, RegisterSerializer, CustomTokenObtainPairSerializer
from .models import User


class RegisterView(CreateAPIView):
    """Foydalanuvchini ro‘yxatdan o‘tkazish"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = True  # Foydalanuvchini avtomatik faollashtirish
        user.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    """JWT Token olish uchun maxsus view"""
    serializer_class = CustomTokenObtainPairSerializer


class UserListCreateView(generics.ListCreateAPIView):
    """Foydalanuvchilar ro‘yxatini olish va yaratish"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Bitta foydalanuvchini olish, o‘zgartirish va o‘chirish"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
