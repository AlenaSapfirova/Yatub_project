from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import Group, Post


def group_posts(requets, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
              }
    return render(requets, 'posts/group_list.html', context)


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
