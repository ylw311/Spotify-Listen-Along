from django.shortcuts import render
from rest_framework import generics 
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# view set up to return all of rooms
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer