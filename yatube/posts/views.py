from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')


def group_posts(requets, any_slug):
    return HttpResponse(f'Чат сообщества {any_slug}')
