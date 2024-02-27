from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EmployeeSerializer,CitySerializer,DistrictSerializer
from .models import  Employee,City,District
from django.db.models import Q

# Create your views here.
class EmployeeUpdate(APIView):
    def post(self, request):
        id=request.data['id']
        q=Employee.objects.get(id=id)
        q.name=request.data['name']
        q.save()
        # data_keys=request.data.keys()
        # for i in data_keys:
        #     print(i)
        #     print(q.i)
            # print(q.i)
            # q.i=request.data[i]
            
        # ser=EmployeeSerializer(q,data=request.data,partial=True)
        # print('ser,',ser)
        # if ser.is_valid():
        #     ser.save()
            # return Response(ser.data)
        return Response({"data":'ok'})
        
class EmployeeGet(APIView):
    def post(self,request):
        # print('keys', request.data.keys())
        # print('values',request.data.values())
        name=request.data.get('name')
        email=request.data.get('email')
        contact=request.data.get('contact')
        address=request.data.get('address')
        age=request.data.get('age')
        
        kwargs={}
        if name:
            kwargs['name']=name
        if email:
            kwargs['email']=email
        if contact:
            kwargs['contact']=contact 
        if address:
            kwargs['address']=address
        if age:
            kwargs['age']=age
        q=Employee.objects.filter(**kwargs) 
        ser=EmployeeSerializer(q,many=True)  
        print(ser)    
        return Response(ser.data)

class EmployeePost(APIView):
    def post(self, request):
        name=request.data.get('name')
        email=request.data.get('email')
        contact=request.data.get('contact')
        address=request.data.get('address')
        age=request.data.get('age')
        
        kwargs={}
        if name:
            kwargs['name']=name
        if email:
            kwargs['email']=email
        if contact:
            kwargs['contact']=contact 
        if address:
            kwargs['address']=address
        if age:
            kwargs['age']=age
        q=Employee.objects.create(**kwargs)
        return Response({"data":"created"})
            
class CityGet(APIView):
    def post(self,request):
        q=City.objects.all()
        ser=CitySerializer(q,many=True)
        return Response(ser.data)
    
class DistrictGet(APIView):
    def post(self,request):
        q=District.objects.all()
        ser=DistrictSerializer(q,many=True)
        return Response(ser.data)
    
# class GetAllArea(APIView):
#     def post(self,request):
        
#         city=request.data.get('city_name')
#         district=request.data.get('dist_name')
#         state=request.data.get('state_name')
#         # kwargs={}
#         # if city:
#         #     kwargs['city']=city
#         # if district:
#         #     kwargs['district_name']=district
#         # if state:
#         #     kwargs['state_name']=state
#         list=[]  
#         if city:
#             list.append('city')
#         if district:
#             list.append('district')
#         if state:
#             list.append('state')
        
#         if 'city' not in list and 'district' not in list and 'state' not in list:
#             c=City.objects.all()
        
#         if 'city' and 'district' and 'state' in list:
#             c=City.objects.filter(city_name=city,district__dist_name=district,district__state__state_name=state)
            
#         if 'city' in  list and "district" not in list and "state" not in list:
#             c=City.objects.filter(city_name=city)

#         if 'city' and 'state' in list and "district" not in list:  
#             c=City.objects.filter(city_name=city,district__state__state_name=state)
        
#         if 'city' and 'district' in list and "state" not in list:
#             c=City.objects.filter(city_name=city,district__dist_name=district)
                
#         if 'district' in list and "city" not in list and "state" not in list:
#             c=City.objects.filter(district__dist_name=district)
            
#         if 'district' and 'state' in list and "city" not in list:
#             c=City.objects.filter(district__dist_name=district,district__state__state_name=state)
            
#         if 'state' in list and "city" not in list and "district" not in list:
#             c=City.objects.filter(district__state__state_name=state)
        
#         ser=CitySerializer(c,many=True)
#         if ser.data:
#             return Response(ser.data)
#         else:
#             message={"message":"no data"}
#             return Response(message)

class GetAllArea(APIView):
    def post(self,request):
        
        city=request.data.get('city_name')
        district=request.data.get('dist_name')
        state=request.data.get('state_name')
        def filter_cities(city_name=None, dist_name=None, state_name=None):
            queryset = City.objects.all()
            print('inside fun')
            if city_name:
                queryset = queryset.filter(city_name__icontains=city_name)

            if dist_name:
                queryset = queryset.filter(district__dist_name__icontains=dist_name)

            if state_name:
                queryset = queryset.filter(district__state__state_name__icontains=state_name)
            
            return queryset
        q=filter_cities(city,district,state)
        ser=CitySerializer(q,many=True)
        if ser.data:
            return Response(ser.data)
        else:
            message={"message":"no data"}
            return Response(message)