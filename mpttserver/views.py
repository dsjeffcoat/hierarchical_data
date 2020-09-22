from django.shortcuts import render
from .models import Genre

# Create your views here.

def shows_genres(request):
    all_genres = Genre.objects.all()
    return render(request, 'index.html', { 'genres': all_genres })