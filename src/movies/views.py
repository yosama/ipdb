from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib import messages

from movies.forms import MovieForm
from movies.models import Movie


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world!")
    else:
        return HttpResponse("Hello " + name)


@login_required
def home(request):
    movies = Movie.objects.all().order_by("-release_date")[:5]
    context = {"movies": movies}

    return render(request, "home.html", context)


@login_required
def movie_detail(request, pk):
    possible_movies = Movie.objects.filter(pk=pk).select_related("category")

    if len(possible_movies) == 0:
        return render(request, "404.html", status=404)
    else:
        movie = possible_movies[0]
        context = {"movie": movie}
        return render(request, "movie_detail.html", context)


class CreateMovieView(LoginRequiredMixin, View):

    def get(self, request):
        form = MovieForm()

        return render(request, "movie_form.html", {"form": form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            form = MovieForm()
            url = reverse("movie_detail_page", args=[movie.pk])
            message = "Movie created successfully"
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)

        return render(request, "movie_form.html", {"form": form})



