from django.urls import path
from .import views

urlpatterns=[
    path('gallery/',views.product_list,name="gallery")
]