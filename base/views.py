from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import Room
#Create yout views

# rooms = [
#     {'id': 1, 'name':'Lets learn python!'},
#     {'id': 2, 'name':'Design with me!'},
#     {'id': 3, 'name':'Front end evelopers'},
#     {'id': 4, 'name':'Hi all'},
# ]


classes = [
    {'id': 1, 'n':'this is class 1'},
    {'id': 2, 'n':'this is class 2'},
    {'id': 3, 'n':'this is class 3'},
    {'id': 4, 'n':'this is class 4'},
]



def home(request):
    rooms = Room.objects.all()
    #Context dictionary to pass the values
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)
  
  

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,'base/room.html',context)


def clas (request):
    return render(request, 'class.html', {'cl':classes})