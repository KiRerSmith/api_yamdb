from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews',
    views.ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    views.CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]
