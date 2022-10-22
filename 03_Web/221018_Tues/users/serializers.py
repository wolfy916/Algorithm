from rest_framework import serializers
from .models import User

class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'