<<<<<<< HEAD
from random import randint

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.tokens import AccessToken
from reviews.models import Category, Comment, Genre, Review, Title, User

from .pagination import UserPagination
from .permissions import IsAdmin, IsOwnerOrReadOnly, IsModerator
from .serializers import (CreateAndGetCode, GetTokenSerializer, MeSerializer,
                          UserSerializer, CommentSerializer, ReviewSerializer)


@api_view(['POST'])
def create_and_get_code(request):
    serializer = CreateAndGetCode(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    username = serializer.validated_data.get('username')
    confirmation_code = randint(10000, 99999)
    message = f'Ваш код {confirmation_code}'
    send_mail(
        subject='Код подтверждения для YAMDB',
        message=message,
        from_email='admin@yamdb.ru',
        recipient_list=[email]
    )
    User.objects.create(username=username, email=email, code=confirmation_code)
    return Response(
        {'email': f'{email}', 'username': f'{username}'},
        status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request):
    serializer = GetTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    code = serializer.validated_data.get('confirmation_code')
    if not User.objects.filter(username=username).exists():
        return Response(
            'Пользователь не найден',
            status=status.HTTP_404_NOT_FOUND)
    user = User.objects.get(username=username)
    if user.code == code:
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response(
        'Отсутствует обязательное поле или оно некорректно',
        status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = (IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()


class APIMe(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(User, id=request.user.id)
            serializer = MeSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            'Необходима авторизация',
            status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(User, id=request.user.id)
            serializer = MeSerializer(user, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        return Response(
            'Необходима авторизация',
            status=status.HTTP_401_UNAUTHORIZED)
=======
from django.shortcuts import get_object_or_404
from reviews.models import Category, Comment, Genre, Review, Title, User
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .serializers import CommentSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly, IsModerator
>>>>>>> d3737c12f4e6f58f7e54ef10e5bc580632cf75ab


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [
        IsOwnerOrReadOnly,
        IsModerator,
<<<<<<< HEAD
        IsAdmin]
=======
        permissions.IsAdminUser]
>>>>>>> d3737c12f4e6f58f7e54ef10e5bc580632cf75ab

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
<<<<<<< HEAD
        IsAdmin]
=======
        permissions.IsAdminUser]
>>>>>>> d3737c12f4e6f58f7e54ef10e5bc580632cf75ab

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
