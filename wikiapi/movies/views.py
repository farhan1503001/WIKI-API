from django.shortcuts import render
from .serializers import MovieSerialize
from .models import Movies
from rest_framework import viewsets
# Create your views here.
class Movie_view(viewsets.ModelViewSet):
    queryset=Movies.objects.all() #Literally the database model
    serializer_class=MovieSerialize#The class which will serialize
