from rest_framework import serializers
from django.db.models import fields
from .models import Student , Student2

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Student
        fields=['id','name','age','course']
    

class Student2Serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Student2
        fields=['id','name','age','course','roll_no']
    