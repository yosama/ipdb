from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Movie
from movies.permissions import MoviesPermission
from movies.serializers import MovieSerializer, MoviesListSerializer


class MovieListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == "GET" else MovieSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MovieDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviesPermission]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)