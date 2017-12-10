from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world!")
    else:
        return HttpResponse("Hello " + name)

def home(request):
    movies = Movie.objects.all().order_by("-realease_date")[:5]
    context = {"movies": movies}

    return render(request, "home.html", context)
