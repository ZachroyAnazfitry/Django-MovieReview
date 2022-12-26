from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import get_object_or_404

# Create your views here.
# home page test
# def home(request):
#     return HttpResponse('this is home page')

# home page html file
def home(request):
    # retrieve value from request object and passsed searcTerm into template
    searchTerm = request.GET.get('searchMovie')

    # find movie using search bar
    if searchTerm:
        movies = Movie.objects.filter(title__icontains = searchTerm)
    else:
        movies = Movie.objects.all()

    # grab and pass all objects in movies admin
    # movies = Movie.objects.all()

    return render(request, 'home.html', {
        
        'name':'Zach',
        'searchTerm':searchTerm, 
        'movies': movies
    })

# about page
def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

# signup page
def signup(request):
    email   = request.GET.get('email')
    return render(request,'signup.html', {'email':email})

# detail function
# to carry movie_id
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {
        'movie':movie
    })