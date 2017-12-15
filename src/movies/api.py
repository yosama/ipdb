from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListAPI(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return  Response(serializer.data)