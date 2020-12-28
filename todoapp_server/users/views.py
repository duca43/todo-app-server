from rest_framework import viewsets, mixins
from .serializers import UserSerializer, User

class UserViewSet(mixins.CreateModelMixin,
                viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer