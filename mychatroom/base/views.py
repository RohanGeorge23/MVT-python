from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
rooms = [
    {'id':1,'name':'Lets Learn Python'},
    {'id':7,'name':'rg24'},
    {'id':42,'name':'sai'}, 
]


def home(request):
    context = {'rooms': rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i 
    context = {'room': room}
    return render(request,'base/room.html')