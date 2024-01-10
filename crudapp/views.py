# views.py

from rest_framework import generics
from .models import Gamer, Videogame
from .serializer import GamerSerializer, VideogameSerializer

class GamerListCreateView(generics.ListCreateAPIView):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer

class VideogameListCreateView(generics.ListCreateAPIView):
    queryset = Videogame.objects.all()
    serializer_class = VideogameSerializer
