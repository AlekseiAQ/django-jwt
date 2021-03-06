from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = [
            "title",
            "person",
            "due_to",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        tasks = serializers.PrimaryKeyRelatedField(
            many=True, queryset=Task.objects.all()
        )
        model = User
        fields = [
            "person",
            "password",
        ]
