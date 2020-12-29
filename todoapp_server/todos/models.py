from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Todo(models.Model):
    NORMAL_PRIORITY = 'NP'
    MEDIUM_PRIORITY = 'MP'
    HIGH_PRIORITY = 'HP'

    PRIORITY_CHOICES = [
        (NORMAL_PRIORITY, 'Normal'),
        (MEDIUM_PRIORITY, 'Medium'),
        (HIGH_PRIORITY, 'High'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=NORMAL_PRIORITY)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)