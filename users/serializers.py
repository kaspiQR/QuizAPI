from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('id', 'phone_number', 'username', 'password')

