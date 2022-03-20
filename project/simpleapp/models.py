from django.db import models
from django.template.backends import django
from django_filters import DateFilter


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name.title()}'
