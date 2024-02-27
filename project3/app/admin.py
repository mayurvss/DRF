from django.contrib import admin
from .models import Employee,EmployeeTask

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','gender','designation']

@admin.register(EmployeeTask)
class EmployeeTaskAdmin(admin.ModelAdmin):
    list_display=['id','task_name','employee','task_desc', 'created_date','deadline']