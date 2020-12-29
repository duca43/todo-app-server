from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.decorators import action
from .serializers import UserSerializer, User

class UserViewSet(mixins.CreateModelMixin,
                viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.data)
        return Response(status=HTTP_201_CREATED)

    @action(detail=False, url_path='me', permission_classes=[IsAuthenticated]) 
    def get_current_user(self, request):          
        response_serializer = UserSerializer(request.user)
        return Response(response_serializer.data, HTTP_200_OK)