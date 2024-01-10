from django.db import models

# Create your models here.
from django.db import models

class Gamer (models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(max_length=277, verbose_name="Email")
    age = models.IntegerField(max_length=3, verbose_name="Age")
    email = models.EmailField(max_length=277, verbose_name="Email")
    nationality= models.CharField(max_length=100, verbose_name="Nationality")
    like= models.IntegerField(max_length=100000, verbose_name="Like")
    dislike= models.IntegerField(max_length=100000, verbose_name="Dislike")
    playlist= models.CharField(max_length=100000, verbose_name="Playlist")
    wishlist= models.CharField(max_length=100000, verbose_name="Wishlist")
    
    
    


    

    def __str__(self):
        return str(self.id)
