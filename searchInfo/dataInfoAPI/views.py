from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from dataInfo.models import User
from .serializers import UserSerializer, DocumentSerializer
from dataInfo.models import UserManager, Documents, DocumentManager
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.renderers import TemplateHTMLRenderer
from dataInfo.forms import UploadFileForm
from django.core.files.storage import FileSystemStorage

import datetime

# Create your views here.

@api_view(['POST'])

@csrf_exempt

def login_view(request):
    email=request.data.get('email')
    password = request.data.get('password')
    user=authenticate(request, email=email, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        serializer= UserSerializer(user)
        #renderer_classes = [TemplateHTMLRenderer]
        #request.session['_old_post'] = request.POST  
        request.session['user'] = serializer.data 
        if serializer.data['is_staff'] is True:
            return redirect('adminPage')
               

        return redirect("homeUser")
        #return Response({
            #'token': token.key,
            #'user_id': user.id,
            #'email': user.email
        #})
    
    else:
        return Response({'error': 'Invalid email or password'}, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
@csrf_exempt
def adminUser_view(request):
    user=request.session['user']
    users=User.objects.all()
    user_serializer=UserSerializer(users, many=True)
    print(user_serializer.data)
    return render(request,'adminUser.html',{'users':user_serializer.data})


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def homeUser_view(request):
    data=request.session['user']    
    documents=Documents.objects.filter(id_user=data['id'])
    doc_serializer=DocumentSerializer(documents, many=True)
    print(doc_serializer.data)
    return render(request,'homeUser.html',{'user':data, 'documents':doc_serializer.data})







@api_view(['POST'])
@csrf_exempt
def logout_view(request):
    logout(request)
    request.session['user']= None
    #request.user.auth_token.delete()
    return redirect ('home')


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
    
    email=request.POST.get('email')
    password=request.POST.get('password')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    user=User.objects.create_user(email, password, first_name, last_name)
    serializer=UserSerializer(user)
   

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
@csrf_exempt
def uploadFile_view(request):
    if request=='POST':
        form=UploadFileForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('homeUser')
    else:
        form=UploadFileForm()
    data=request.POST.get('user')
    return render(request,'uploadFile.html',{'data':data,'form':form})

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
@csrf_exempt
def upload(request):
    context = {}
    if request.method == 'POST':
        
        uploaded_file = request.FILES['my_file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

        user=request.session['user']
        print(user["id"])
        document=Documents.objects.upload_document(uploaded_file.name, 'txt', datetime.date.today(),str(user['id']))
        request.data.update({"id_user": str(user['id']), "url":context['url']})
        print(context['url'])
        serializer=DocumentSerializer(data=request.data)
        #print(serializer.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
    return render(request, 'uploadSuccess.html', context)