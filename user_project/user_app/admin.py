from django.contrib import admin
from .models import UserRegister, UserRole

# Register your models here.
@admin.register(UserRegister)
class UserRegisterAdmin(admin.ModelAdmin):
    list_display=['id','name','mobile_no','email_id', 'address']
    
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display=['roll', 'user']