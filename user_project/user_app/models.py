from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name=models.CharField( max_length=50)
    email_id=models.EmailField(max_length=50)
    mobile_no=models.CharField(max_length=100)
    address=models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        db_table='user_register'
        
class UserRole(models.Model):
    roll=models.CharField(max_length=50)
    user=models.ForeignKey('UserRegister', related_name='user_role', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.roll
    class Meta:
        db_table='user_role'
    
