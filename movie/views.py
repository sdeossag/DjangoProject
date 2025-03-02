from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64




from .models import Movie
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')

    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'SearchTerm': searchTerm, 'movies': movies})

def about(request):
    return render(request, 'about.html',)
import matplotlib.pyplot as plt
import matplotlib
import io
import base64
from django.shortcuts import render
from movie.models import Movie

import matplotlib.pyplot as plt
import matplotlib
import io
import base64
from django.shortcuts import render
from movie.models import Movie

def statistics_view(request):
    matplotlib.use('Agg')

    # Obtener todas las películas
    all_movies = Movie.objects.all()

    # Diccionarios para almacenar la cantidad de películas por género y por año
    movie_counts_by_genre = {}
    movie_counts_by_year = {}

    # Recorrer todas las películas y contar por género y por año
    for movie in all_movies:
        # Procesar género
        genres = movie.genre.split(",") if movie.genre else ["None"]
        first_genre = genres[0].strip()  # Solo primer género
        
        if first_genre in movie_counts_by_genre:
            movie_counts_by_genre[first_genre] += 1
        else:
            movie_counts_by_genre[first_genre] = 1

        # Procesar año
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

    # **Gráfica 1: Películas por año**
    plt.figure(figsize=(10, 5))
    bar_positions = range(len(movie_counts_by_year))
    plt.bar(bar_positions, movie_counts_by_year.values(), width=0.5, align='center', color='royalblue')
    plt.title('Movies per year', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of movies', fontsize=12)
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    # Guardar la primera gráfica en base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    graphic_year = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # **Gráfica 2: Películas por género**
    plt.figure(figsize=(10, 5))
    bar_positions = range(len(movie_counts_by_genre))
    plt.bar(bar_positions, movie_counts_by_genre.values(), width=0.5, align='center', color='lightcoral')
    plt.title('Movies per genre', fontsize=14)
    plt.xlabel('Genre', fontsize=12)
    plt.ylabel('Number of movies', fontsize=12)
    plt.xticks(bar_positions, movie_counts_by_genre.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    # Guardar la segunda gráfica en base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    graphic_genre = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Renderizar la plantilla con ambas gráficas
    return render(request, 'statistics.html', {'graphic_year': graphic_year, 'graphic_genre': graphic_genre})




def signup(request):
    email = request.POST.get('email')
    return render(request, 'signup.html', {'email': email})