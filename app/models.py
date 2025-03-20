from datetime import datetime
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    short_dec = models.CharField(max_length=200)
    desc = models.TextField()
    author = models.CharField(max_length=100, default='admin')
    image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Sponsors(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to="images/")

    def __str__(self):
        return self.name


class Date(models.Model):
    date = models.DateField(auto_now_add=True)
