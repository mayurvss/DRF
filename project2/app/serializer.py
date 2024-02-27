from django.db.models import fields
from rest_framework import serializers
from .models import Employee,State,District,City

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['name','email', 'contact','address','age']
        

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields='__all__'
        
class DistrictSerializer(serializers.ModelSerializer):
    # citys=serializers.StringRelatedField(many=True)
    state = serializers.StringRelatedField(source='state.state_name')    
    class Meta:
        model=District
        fields=('id','dist_name','state')
        
class CitySerializer(serializers.ModelSerializer):
    # district = serializers.PrimaryKeyRelatedField(source='district.id', read_only=True)
    state = serializers.StringRelatedField(source='district.state.state_name')
    district=serializers.StringRelatedField()
    # district=serializers.SlugRelatedField(queryset=District.objects.all(), 
    #     slug_field='dist_name')

    class Meta:
        model=City
        fields=('id','city_name','district','state')
    