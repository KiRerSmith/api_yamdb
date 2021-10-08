from django.urls import include, path
from rest_framework import routers

from .views import APIMe, create_and_get_code, UserViewSet, get_token, UsernameViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='userviewset')
router.register(r'^users/(?P<username>[\w.@+-]+$)', UsernameViewSet, basename='UsernameViewSet')

urlpatterns = [
    path('v1/auth/signup/', create_and_get_code, name='create_and_get_code'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/users/me/', APIMe.as_view(), name='apime')
]
