from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):

    # pass News data from Admin
    newss = News.objects.all()


    return render(request,'news.html', {
        'newss':newss

    })