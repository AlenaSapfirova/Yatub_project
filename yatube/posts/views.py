from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(requets, any_slug):
    return HttpResponse(f'Чат сообщества {any_slug}')
