from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    return render(request, 'articles/index.html', context={'title': 'the articles'})