

# Create your models here.
from django.db import models


class Videogame(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)  # Add the missing title field

    def __str__(self):
        return self.title

class Gamer (models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    username = models.CharField(max_length=15, verbose_name="Username")
    password = models.CharField(max_length=27, verbose_name="Password")
    age = models.IntegerField(max_length=3, verbose_name="Age")
    email = models.EmailField(max_length=277, verbose_name="Email")
    nationality= models.CharField(max_length=100, verbose_name="Nationality")
    like= models.ManyToManyField(Videogame, related_name='users_like', blank=True)
    playlist= models.ManyToManyField(Videogame, related_name='users_playlist', blank=True)
    wishlist= models.ManyToManyField(Videogame, related_name='users_wishlist', blank=True)
    
# models.py





    


    


