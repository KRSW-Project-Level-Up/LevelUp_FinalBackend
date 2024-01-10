# urls.py

from django.urls import path
from .views import GamerListCreateView, VideogameListCreateView

urlpatterns = [
    path('gamers/', GamerListCreateView.as_view(), name='gamer-list-create'),
    path('videogames/', VideogameListCreateView.as_view(), name='videogame-list-create'),
]
