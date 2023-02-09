from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Gazeta, Yangiliklar
def newDetail(request, pk):
    post = Yangiliklar.objects.get(pk=pk)
    context = {
        'yangilik': post
    }
    return render(request, 'news_detail.html', context)

def newspaperDetail(request, pk):
    post = Gazeta.objects.get(pk=pk)
    context = {
        'gazeta': post
    }
    return render(request, 'post_detail.html', context)

def news(request):
    newspapers = Gazeta.objects.all()
    news = Yangiliklar.objects.all()
    context = {
        'news': news,
        'newspapers': newspapers
    }
    return render(request, 'home.html', context)

