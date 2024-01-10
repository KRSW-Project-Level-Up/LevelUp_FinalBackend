from django.contrib import admin
from .models import Gamer

@admin.register(Gamer)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email","age", "nationality","like","dislike","playlist","wishlist"]
