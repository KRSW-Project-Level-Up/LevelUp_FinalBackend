from django.shortcuts import render
from .models import Gamer
from django.contrib import messages
from django.db.models import Q


def index(request):
    gamers = Gamer.objects.all()
    search_query = ""
    if request.method == "POST": 
        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            nationality= request.POST.get("nationality")
            like= request.POST.get("like")
            dislike= request.POST.get("dislike")
            playlist= request.POST.get("playlist")
            wishlist= request.POST.get("wishlist")
            
            Gamer.objects.create(
                name=name,
                email=email,
                age=age,
                nationality=nationality,
                like = like,
                dislike=dislike,
                playlist=playlist,
                wishlist=wishlist
            )
            messages.success(request, "User added successfully")
    
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            nationality= request.POST.get("nationality")
            like= request.POST.get("like")
            dislike= request.POST.get("dislike")
            playlist= request.POST.get("playlist")
            wishlist= request.POST.get("wishlist")
            gamer = Gamer.objects.get(id=id)
            gamer.name = name
            gamer.email = email
            gamer.age=age
            gamer.nationality=nationality
            gamer.like=like
            gamer.dislike=dislike
            gamer.playlist=playlist
            gamer.wishlist=wishlist
            gamer.save()
            messages.success(request, "User updated successfully")
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Gamer.objects.get(id=id).delete()
            messages.success(request, "User deleted successfully")
        
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            gamers = Gamer.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

    context = {"gamers": gamers, "search_query": search_query}
    return render(request, "index.html", context=context)
