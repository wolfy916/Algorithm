from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Club
from .serializers import ClubListSerializer
from users.serializers import ClubUserSerializer

# rest api api_view
@api_view(['GET', 'POST'])
def club_list(request):
    if request.method == 'GET':
        clubs = Club.objects.all()
        
        # serializer = ClubListSerializer(clubs, many=True)
        serializer = ClubUserSerializer(clubs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClubListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


