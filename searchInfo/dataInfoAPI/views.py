from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from dataInfo.models import User
from .serializers import UserSerializer
from dataInfo.models import UserManager
# Create your views here.

@api_view([ 'POST'])
@csrf_exempt
def login_view(request):
    email=request.data.get('email')
    password = request.data.get('password')
    user=authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        serializer= UserSerializer(user)
        return Response (serializer.data)
    
    else:
        return Response({'error': 'Invalid email or password'}, status= status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@csrf_exempt
def logout_view(request):
    logout(request)
    return Response ({'success': 'Logged out successfully'})


@api_view(['POST'])
@csrf_exempt
def signup_view(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@csrf_exempt
def create_user_view(request):
    
    username=request.POST.get('email')
    password=request.POST.get('password')
    user=User.objects.create_user(username, password)
    serializer=UserSerializer(user)

    

    return Response(serializer.data, status=status.HTTP_201_CREATED)
