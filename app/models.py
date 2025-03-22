from django.db import models
from django.contrib.auth.models import User


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
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    liked_users = models.ManyToManyField(User, related_name='liked_news', blank=True)
    disliked_users = models.ManyToManyField(User, related_name='disliked_news', blank=True)

    def __str__(self):
        return self.title


class Sponsors(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to="images/")

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    view = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} -> {self.message}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    news = models.ForeignKey(News, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} --> {self.created_at}"

    class Meta:
        ordering = ['-created_at']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='images/default.png')

    def __str__(self):
        return self.user.username
