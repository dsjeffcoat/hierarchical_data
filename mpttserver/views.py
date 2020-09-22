from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Genre
from .forms import CreateGenreForm

# Create your views here.

def shows_genres(request):
    all_genres = Genre.objects.all()
    return render(request, 'index.html', { 'genres': all_genres })

def add_genre(request):
    if request.method == 'POST':
        form = CreateGenreForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            genre = Genre.objects.create(
                name=data.get('name'),
                parent=data.get('parent')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = CreateGenreForm()
    return render(request, 'generic_form.html', {'form': form})

def login(request):
    pass

def logout(request):
    pass