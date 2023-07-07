from django.urls import path
from .views import userProfile

urlpatterns = [
    path('profile/',userProfile),
    path('',userProfile)
    
]
