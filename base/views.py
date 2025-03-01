from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    
    return render(request, 'base/room_form.html',context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html',{'obj':room})