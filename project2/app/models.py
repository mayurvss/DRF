from django.db import models

# Create your models here.cd
class Employee(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=90)
    contact=models.IntegerField()
    address=models.TextField()
    age=models.IntegerField()
    
class State(models.Model):
    state_name=models.CharField(max_length=50)

    def __str__(self):
        return self.state_name
    
class District(models.Model):
    dist_name=models.CharField( max_length=50)
    state=models.ForeignKey("State",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dist_name
    
    
class City(models.Model):
    city_name=models.CharField(max_length=50)
    district=models.ForeignKey("District",on_delete=models.CASCADE,related_name='citys')
    
    def __str__(self):
        return self.city_name
    