from rest_framework import serializers
from .models import Todo

class CreateTodoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'completed']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'priority', 'completed', 'user']
