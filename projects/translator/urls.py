from django.urls import path 
from .views import *
  
urlpatterns = [ 
    path('translator/',home,name="translator"), 
]