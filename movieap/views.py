from django.shortcuts import render

# Create your views here.
from .models import Movie
from rest_framework.viewsets import ModelViewSet
from .serializers import MoviesSerializer

class MovieOperations(ModelViewSet):
    queryset = Movie.objects.all()

    serializer_class = MoviesSerializer
    # authentication_classes = (TokenAuthentication,)