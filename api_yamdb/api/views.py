from reviews.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.generics import CreateAPIView


from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
