from django.shortcuts import render
from rest_framework.decorators import api_view
# api 리턴
from rest_framework.response import Response
# Create your views here.
from django.shortcuts import get_object_or_404
from users.models import User
from .serializers import UserListSerializer, UserSerializer

# REST API 선언시
# @api_view 데코레이터를 활용 

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        
        # 파이썬에서만 활용하는 형태
        # print(users)
        # 리스트형태로 보기쉽게 직렬화를해서 
        print(request.GET)
        search = request.GET.get('search')
        if search is not None:
            users = User.objects.filter(first_name__contains=search)
        else:
            users = User.objects.all()

        serializer = UserListSerializer(users, many=True)
        # print(serializer)
        return Response(serializer.data)
    elif request.method == 'POST':
        # form
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        data = {
            'delete':f'데이터 {user_pk}번이 삭제되었습니다',
            'success':True
        }
        return Response(data)


@api_view(['POST'])
def user_club(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == "POST":
        print(request.data.get('club'))
        club = request.data.get('club')
        # 브릿지테이블에 값생성
        user.clubs.add(club)
        
        data = {
            'success':True
        }
        
        return Response(data)

