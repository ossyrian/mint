from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, GuildViewSet, UserViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'guilds', GuildViewSet, basename='guild')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
