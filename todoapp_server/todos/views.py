from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .models import Todo
from .serializers import CreateTodoSerializer, TodoSerializer

class TodoViewSet(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return CreateTodoSerializer
        return TodoSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_todo = Todo.objects.create(**serializer.data, user=request.user)
        response_serializer = TodoSerializer(created_todo)
        return Response(response_serializer.data, status=HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response_serializer = TodoSerializer(self.get_object())
        return Response(response_serializer.data, status=HTTP_200_OK)


