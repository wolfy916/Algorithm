from rest_framework import serializers

from .models import Club
# from users.serializers import UserListSerializer

# user의 serialzers에서도 clubListCSerializer를 가져온다
# club의 serialzers에서도 User에대한 내용을 가져오려고하니까
# 서로 순환참조 -> 에러 발생 

# user의 serialzers에 새로 시리얼라이즈를 만들어준다. 

class ClubListSerializer(serializers.ModelSerializer):
    # related_name에 users라고 명시 
    # UserListSerializer
    # users = UserListSerializer(many=True)
    class Meta:
        model = Club
        fields = '__all__'
