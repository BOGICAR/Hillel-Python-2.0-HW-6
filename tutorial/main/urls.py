from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('home', views.home)
    # path('movies',
    #      views.MovieList.as_view(),
    #      name='MovieList'),
]
