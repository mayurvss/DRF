from django.contrib import admin
from .models import Employee,State,District,City

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','email','contact','address','age']

@admin.register(State)    
class StateAdmin(admin.ModelAdmin):
    list_display=['id','state_name']
    
@admin.register(District)    
class DistrictAdmin(admin.ModelAdmin):
    list_display=['id','dist_name']
    
@admin.register(City)    
class CityAdmin(admin.ModelAdmin):
    list_display=['id','city_name']
    