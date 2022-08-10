from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Quotes(models.Model):
    text = models.TextField(unique=True)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.authors.name
