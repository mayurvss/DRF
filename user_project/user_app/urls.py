from django.contrib import admin
from django.urls import path
from .views import AddUser,GetUser,AddRole
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    
    path('adduser/', AddUser.as_view()),
    path('getuser/',GetUser.as_view()),
    path('addrole/', AddRole.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify')
   
]
