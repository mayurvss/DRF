from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    course=models.CharField(max_length=50)
    
     
    def __str__(self):
        return self.name
    
class Student2(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    course=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
    