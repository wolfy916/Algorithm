from rest_framework import serializers
from .models import Club

class ClubListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'