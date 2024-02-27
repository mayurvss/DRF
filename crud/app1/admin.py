from django.contrib import admin
from .models import Student,Student2

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age', 'course']
    
@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id','name','age', 'course','roll_no']