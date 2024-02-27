
from django.contrib import admin
from django.urls import path,include
from app import  views


urlpatterns=[
    
    path('employees/', 
        views.employee_list, 
        name = 'employee-list'), 
    path('employees/<int:pk>/', 
        views.employee_detail, 
        name='employee-detail'), 
    path('task/', 
        views.employeetask_list, 
        name = 'employeetask-list'), 
    path('task/<int:pk>/', 
        views.employeetask_detail, 
        name='employeetask-detail'),
    
 ]