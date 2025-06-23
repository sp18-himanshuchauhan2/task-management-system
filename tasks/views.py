from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def register_user(request):
    data = request.data
    serializer = RegisterSerializer(data = data)
    
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user = user)
        return Response({'token': token.key})
    
    return Response(serializer.errors)
