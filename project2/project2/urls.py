"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import EmployeeUpdate,EmployeeGet,EmployeePost,CityGet,DistrictGet,GetAllArea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeupdate/', EmployeeUpdate.as_view
         ()),
    path('employeeget/', EmployeeGet.as_view
         ()),
    path('employeepost/', EmployeePost.as_view
         ()),
    path('cityget/', CityGet.as_view
         ()),
    path('districtget/', DistrictGet.as_view
         ()),
    
    path('getallarea/', GetAllArea.as_view
         ()),
]
