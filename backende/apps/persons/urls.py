from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    UserViewSet,
    HistoricalPersonViewSet,
    FavoriteViewSet,
    RegisterView,  # 👈 добавили
    index,
)

from django.conf import settings
from django.conf.urls.static import static

# 🔁 Router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'persons', HistoricalPersonViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    # 🔥 тест
    path('', index, name='index'),

    # 🔐 AUTH
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📦 API
    path('', include(router.urls)),
]

# 📁 MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)