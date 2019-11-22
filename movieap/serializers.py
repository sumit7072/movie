from .models import Movie
from rest_framework.serializers import ModelSerializer


class MoviesSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_names', 'actor_names')
