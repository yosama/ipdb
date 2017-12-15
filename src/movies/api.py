from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
