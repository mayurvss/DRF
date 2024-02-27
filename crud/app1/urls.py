
from django.urls import path,include
from .views import *

urlpatterns = [
    path('liststudent/',StudentView.as_view()),
    path('detailstudent/<int:pk>/',StudentDetailView.as_view()),
    # all post method api
    path('listall/',StudentGetAll.as_view()),
    path('getlist/<int:pk>/',StudentGet.as_view()),
    path('poststudent/',StudentPost.as_view()),
    path('updatestudent/',StudentPut.as_view()),
    path('partialupdatestudent/',StudentPatch.as_view()),
    path('deletestudent/<int:pk>/',StudentDelete.as_view()),
    
    path('student2-post/', Student2_Post.as_view())
]