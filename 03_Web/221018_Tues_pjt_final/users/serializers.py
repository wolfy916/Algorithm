from rest_framework import serializers
from .models import User
from clubs.models import Club

from clubs.serializers import ClubListSerializer

class UserListSerializer(serializers.ModelSerializer):
    # 원래라면 clubs:[1, 2..] -> 해당 PK를 기반으로 데이터를 가져온다
    clubs = ClubListSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ClubUserSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Club
        fields = '__all__'
