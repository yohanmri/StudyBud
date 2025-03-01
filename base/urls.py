from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    
    #pk means primary key , str means str, int etx can be used
    path('rooms/<str:pk>/',views.room, name="room"),
    path('class/',views.clas, name="classes"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    
    
]
