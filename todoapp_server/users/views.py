from rest_framework import viewsets, mixins
from .serializers import UserSerializer, User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action

class UserViewSet(mixins.CreateModelMixin,
                viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, 
        url_path='me', 
        permission_classes=[IsAuthenticated],
        renderer_classes=[JSONRenderer]) 
    def get_current_user(self, request):          
        response_serializer = UserSerializer(request.user)
        return Response(response_serializer.data, HTTP_200_OK)