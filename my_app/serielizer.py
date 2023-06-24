from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ChatText

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ChatSerializer(serializers.ModelSerializer):
    receiver = UserSerializer()
    sender = UserSerializer()

    class Meta:
        model = ChatText
        fields = ['receiver', 'sender', 'text', 'time']