from django.urls import path
from rest_framework import routers
from .views import TodoViewSet

todoRouter = routers.SimpleRouter()
todoRouter.register(r'todos', TodoViewSet)
