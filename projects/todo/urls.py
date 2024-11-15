from django.urls import path
from todo import views

urlpatterns = [
    path('index/',views.index,name="todo"),
    path('del/<str:item_id>',views.remove,name='del'),
]