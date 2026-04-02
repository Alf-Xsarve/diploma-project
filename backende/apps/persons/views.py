from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    UserSerializer,
    HistoricalPersonSerializer,
    FavoriteSerializer,
    RegisterSerializer,
)

from .models import HistoricalPerson, Favorite


# 🔥 Тест API
def index(request):
    return JsonResponse({"message": "История Кыргызстана в лицах — API работает!"})


# 🔐 РЕГИСТРАЦИЯ + JWT
class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=["Auth"],
        request_body=RegisterSerializer,  # 🔥 ВАЖНО
    )
    def post(self, request):
        print("REQUEST DATA:", request.data)  # 👈 DEBUG

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_201_CREATED)

        print("ERRORS:", serializer.errors)  # 👈 DEBUG

        return Response(serializer.errors, status=400)


# 👤 Пользователи (только админ)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(tags=["Пользователи"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Пользователи"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Пользователи"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Пользователи"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Пользователи"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# 🧠 Исторические личности
class HistoricalPersonViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerson.objects.all()
    serializer_class = HistoricalPersonSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    @swagger_auto_schema(tags=["Исторические личности"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Исторические личности"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Исторические личности"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Исторические личности"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Исторические личности"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# ❤️ Избранное
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(tags=["Избранное"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Избранное"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Избранное"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)