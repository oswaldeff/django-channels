from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


# Create your views here.


def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def chatroom(request, room_name):
    context = {
        'room_name': mark_safe(json.dumps(room_name))
    }
    return render(request, 'chatroom.html', context)