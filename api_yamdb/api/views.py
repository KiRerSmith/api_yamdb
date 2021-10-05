from django.shortcuts import get_object_or_404
from reviews.models import Category, Comment, Genre, Review, Title, User
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .serializers import CommentSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly, IsModerator


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [
        IsOwnerOrReadOnly,
        IsModerator,
        permissions.IsAdminUser]

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        return Review.objects.filter(title=title)

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        get_object_or_404(Title, pk=title_id)
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [
        IsOwnerOrReadOnly,
        IsModerator,
        permissions.IsAdminUser]

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        get_object_or_404(Title, pk=title_id)
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, pk=review_id)
        return Comment.objects.filter(review=review)

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        get_object_or_404(Title, pk=title_id)
        review_id = self.kwargs.get("review_id")
        get_object_or_404(Review, pk=review_id)
        serializer.save(author=self.request.user)
