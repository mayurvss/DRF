from django.shortcuts import render
from .serializer import StudentSerializer,Student2Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Student,Student2
from rest_framework import status

# Create your views here.

class StudentView(APIView):
    def get(self,request):
        st=Student.objects.all()
        ser=StudentSerializer(st, many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    def post(self,request):
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,
                            status=status.HTTP_201_CREATED)
        return Response(ser.errors,
                        status=status.HTTP_400_BAD_REQUEST)
           
class StudentDetailView(APIView):
    def put(self,request,pk=None ):
        st=Student.objects.get(pk=pk)
        ser=StudentSerializer(st,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,
                        status=status.HTTP_400_BAD_REQUEST)
        
                
    def delete(self,request,pk=None):
        st=Student.objects.get(pk=pk)
        st.delete()
        return Response(status=status.HTTP_200_OK)
    
    def patch(self,request, pk=None):
        st=Student.objects.get(pk=pk)
        ser=StudentSerializer(st,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,
                        status=status.HTTP_400_BAD_REQUEST)
        
class StudentGetAll(APIView):
    def post(self,request):
        q=Student.objects.all()
        ser=StudentSerializer(q,many=True)
        return Response(ser.data)
    
class StudentGet(APIView):
    def post(self,request,pk):
        try:
            q=Student.objects.get(pk=pk)
            ser=StudentSerializer(q)
            return Response(ser.data)
        except  ObjectDoesNotExist:
           raise Http404 

class StudentPost(APIView):
    def post(self,request):
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,
                            status=status.HTTP_201_CREATED)
        return Response(ser.errors,
                        status=status.HTTP_400_BAD_REQUEST)
        
class StudentPut(APIView):
    def post(self,request):
        print(request.data)
        id=request.data.get('id')
        st=Student.objects.get(id=id)
        ser=StudentSerializer(st,data=request.data)
        
        print(ser)
        if ser.is_valid():
            ser.save()
            print(ser.data)
            response={"data":"create sucessfully"}
            # return Response(ser.data,status=status.HTTP_201_CREATED)
            return Response(response,status=status.HTTP_201_CREATED)

        return Response(ser.errors,
                        status=status.HTTP_400_BAD_REQUEST)
        
class StudentPatch(APIView):
    def post(self,request):
        # st=Student.objects.get(pk=pk)
        ser=StudentSerializer(st,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,
                        status=status.HTTP_400_BAD_REQUEST)
          
class StudentDelete(APIView):
    def post(self,request,pk):
        q=Student.objects.get(pk=pk)
        q.delete()
        return Response("data deleted")
    

class Student2_Post(APIView):
    def post(self,request):
        roll_no=request.data['roll_no']
        check_rollno=Student2.objects.filter(roll_no=roll_no)
        print('check roll no', check_rollno)
        if check_rollno.exists():
            return Response({'message':'roll no exists'})
        else:
            ser=Student2Serializer(data=request.data)
            print('yes')
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            