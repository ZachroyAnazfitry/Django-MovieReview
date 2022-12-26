from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>', views.detail, name='detail'),
    # <int:movie_id> PK for movie represented as int, carry movie id
]