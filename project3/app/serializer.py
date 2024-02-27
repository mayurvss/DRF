from rest_framework import serializers 
from .models import Employee, EmployeeTask 

class EmployeeSerializer(serializers.ModelSerializer):
    tasks=serializers.StringRelatedField(many=True)
     
    # task=serializers.StringRelatedField(source='tasks.task_name', many=True)
	# tasks=serializers.StringRelatedField()
    class Meta:
	    model = Employee
	    fields = ('pk', 'emp_id', 'name', 'gender', 'designation', 'tasks')

class EmployeeTaskSerializer(serializers.ModelSerializer):
    def get_name_desc(self,obj):
        return f'{obj.task_name} {obj.task_desc}' 
 
    name_desc=serializers.SerializerMethodField(source='get_name_desc')
    
 
    class Meta:
        model = EmployeeTask
        
     
        fields = ('pk','task_name', 'employee', 'task_desc', 'created_date', 'deadline','name_desc')
        
     
    
	