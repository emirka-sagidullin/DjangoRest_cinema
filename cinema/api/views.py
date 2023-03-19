from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *

# Create your views here.

class LCFilmView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class RUDFilmView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class LCGenreView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class RUDGenreView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class LCDirectorView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class RUDDirectorView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class LCPosterView(ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class RUDPosterView(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

