from django.shortcuts import render
from .serializers  import  UserRegisterSerializer,UserRoleSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserRegister 
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AddUser(APIView):
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            # print('serialierdata:', serializer.data)
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AddRole(APIView):
    def post(self,request):
        # user=request.data.get('user')
        # pk=UserRegister.objects.get(pk=user)
        # print(pk)
        # print(request.data)
        serializer=UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    

class GetUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        queryset=UserRegister.objects.all()
        serializer=UserRegisterSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
