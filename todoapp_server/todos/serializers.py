from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'priority', 'priority_value', 'completed', 'user']

    priority_value = serializers.CharField(source='get_priority_display', read_only=True)