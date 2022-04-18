from django.urls import path
from .views import index, chatroom


urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', chatroom, name='chatroom'),
]
