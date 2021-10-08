from django.urls import include, path
from rest_framework import routers

from .views import create_and_get_code, UserViewSet, MeViewSet, get_token

router = routers.DefaultRouter()
router.register('me', MeViewSet, basename='meviewset')
router.register('', UserViewSet, basename='userviewset')

urlpatterns = [
    path('v1/auth/signup/', create_and_get_code, name='create_and_get_code'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/users/', include(router.urls)),
]
