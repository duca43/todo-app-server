from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .models import Todo
from .permission import TodoAccessPermission
from .serializers import CreateTodoSerializer, TodoSerializer

class TodoViewSet(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated, TodoAccessPermission]

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return CreateTodoSerializer
        return TodoSerializer

    def list(self, request):
        user = self.request.user
        user_todos = Todo.objects.filter(user=user)
        response_serializer = TodoSerializer(user_todos, many=True)
        return Response(response_serializer.data, status=HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_todo = Todo.objects.create(**serializer.data, user=request.user)
        response_serializer = TodoSerializer(created_todo)
        return Response(response_serializer.data, status=HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        response_serializer = TodoSerializer(self.get_object())
        return Response(response_serializer.data, status=HTTP_200_OK)


