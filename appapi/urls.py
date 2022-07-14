from django.urls import path
from appapi import views


urlpatterns = [
    path('register/', views.UserRegistrationAPI.as_view(), name='registration'),
   path('usermanage/<int:id>', views.UserManagemenetAPI.as_view(), name='usermanage'),
  
    
     
]