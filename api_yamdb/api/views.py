from random import randint

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from reviews.models import User

from .pagination import UserPagination
from .permissions import IsAdmin
from .serializers import (CreateAndGetCode, GetTokenSerializer, MeSerializer,
                          UserSerializer)


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
