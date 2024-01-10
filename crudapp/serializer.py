# serializers.py

from rest_framework import serializers
from .models import Gamer, Videogame

class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = '__all__'

class GamerSerializer(serializers.ModelSerializer):
    like = VideogameSerializer(many=True)
    playlist = VideogameSerializer(many=True)
    wishlist = VideogameSerializer(many=True)

    class Meta:
        model = Gamer
        fields = '__all__'
