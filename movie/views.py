from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
# home page
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