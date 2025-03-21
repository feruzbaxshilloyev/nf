from .forms import ContactMessageForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
import datetime


def date_view():
    return datetime.datetime.today()


def index(request):
    ctg = Category.objects.all()
    ctg1 = Category.objects.filter(is_active=True)
    news = News.objects.all().order_by('-created_at')
    popular = News.objects.all().order_by('-views')
    sps = Sponsors.objects.all()
    ctx = {
        'ctg': ctg,
        'ctg1': ctg1,
        'news': news,
        'popular': popular,
        'sps': sps,
        'date': date_view(),
    }
    return render(request, 'index.html', ctx)


def about(request):
    return render(request, 'about.html')


def category(request, pk):
    ctg = Category.objects.get(id=pk)
    ctg1 = Category.objects.filter(is_active=True)
    news = News.objects.filter(category__name=ctg.name).order_by('-created_at')
    idd = ctg.id
    ctx = {
        'ctg': ctg,
        'news': news,
        'ctg1': ctg1,
        'date': date_view(),
        'idd': idd,
    }
    return render(request, 'category.html', ctx)


def news_detail(request, pk):
    news = News.objects.get(id=pk)
    newss = News.objects.all().order_by('-created_at')
    news.views += 1
    news.save()
    ctg = Category.objects.all()
    ctg1 = Category.objects.filter(is_active=True)
    news_ctg = News.objects.filter(category=news.category).order_by('-id')[:4]
    sps = Sponsors.objects.all()
    popular = News.objects.all().order_by('-views')
    ctx = {
        'news': news,
        'ctg': ctg,
        'ctg1': ctg1,
        'news_ctg': news_ctg,
        'date': date_view(),
        'newss': newss,
        'popular': popular,
        'sps': sps,
    }
    return render(request, 'single_page.html', ctx)


def contact1(request):
    news = News.objects.all().order_by('-created_at')
    popular = News.objects.all().order_by('-views')
    ctg = Category.objects.all().order_by('-id')
    ctg1 = Category.objects.filter(is_active=True)
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ContactMessageForm()
    ctx = {
        'ctg': ctg,
        'ctg1': ctg1,
        'news': news,
        'popular': popular,
        'date': date_view(),
        'form': form,
    }

    return render(request, "contact.html", ctx)
