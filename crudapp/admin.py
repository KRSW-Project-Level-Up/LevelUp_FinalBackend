# admin.py

from django.contrib import admin
from .models import Gamer, Videogame

class VideogameAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']  # Customize the fields displayed in the list view
    search_fields = ['title']  # Enable searching by title in the admin interface

@admin.register(Gamer)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name","username","password", "email", "age", "nationality", 'display_likes', 'display_playlist', 'display_wishlist']
    search_fields = ['username','name', 'email', 'playlist__title', 'wishlist__title']  # Enable searching by name, email, playlist title, and wishlist title

    def display_likes(self, obj):
        return ', '.join([str(like.id) for like in obj.like.all()])

    display_likes.short_description = 'Likes'

    def display_playlist(self, obj):
        return ', '.join([str(playlist.id) for playlist in obj.playlist.all()])

    display_playlist.short_description = 'Playlist'

    def display_wishlist(self, obj):
        return ', '.join([str(wishlist.id) for wishlist in obj.wishlist.all()])

    display_wishlist.short_description = 'Wishlist'

# Register the VideogameAdmin class with the Videogame model
admin.site.register(Videogame, VideogameAdmin)
