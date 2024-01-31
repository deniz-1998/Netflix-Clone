from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")

def browse_index(request):
    movies=Movies.objects.all()
    context={}
    search_movie=""
    if request.GET.get("search"):
        search_movie = request.GET.get("search")
        movies=movies.filter(
            Q(filmismi__icontains=search_movie) |
            Q(kategori__name__icontains=search_movie)
        )
    try:
        izleyen=Izlenenler.objects.get(user=request.user)
        izlenen=izleyen.izlenen.all()
        context={
            "izlenen":izlenen,
            "filmler":movies,
            "search_movie":search_movie
        }
    except:
        context={
            "filmler":movies,
            "search_movie":search_movie
        }
       
    return render(request,"browse-index.html",context)