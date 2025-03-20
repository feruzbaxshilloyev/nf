from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    ctg = Category.objects.all()
    ctg1 = Category.objects.filter(is_active=True)
    news = News.objects.all().order_by('-created_at')
    popular = News.objects.all().order_by('-views')
    sps = Sponsors.objects.all()
    dt = Date.objects.all()
    ctx = {
        'ctg': ctg,
        'ctg1': ctg1,
        'news': news,
        'popular': popular,
        'sps': sps,
        'dt': dt,
    }
    return render(request, 'index.html', ctx)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def category(request, id):
    ctg = Category.objects.get(id=id)
    news_ctg = News.objects.filter(category=ctg.name).order_by('-id')
    ctx = {
        'ctg': ctg,
        'news_ctg': news_ctg,
    }
    return render(request, 'category.html', ctx)

