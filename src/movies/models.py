from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True) # Optional

    def __str__(self):
        return self.name


class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    summary = models.TextField()
    director_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)  # save the date when the object is created
    modified_at = models.DateTimeField(auto_now_add=True)  # save the date when the object is updated

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
