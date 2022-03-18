from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    context = {}
    return render(request, 'base/home.html', context)


def veille(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'base/veille_page.html', context)


def article_details(request, id):
    article_detail = Article.objects.get(id=id)
    context = {'article_detail': article_detail}
    return render(request, 'base/article_details.html', context)


def stage_page(request):
    context = {}
    return render(request, 'base/stage_page.html', context)


def cv_page(request):
    context = {}
    return render(request, 'base/cv_page.html', context)
