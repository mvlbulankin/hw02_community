from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = "posts/index.html"
    # posts = Post.objects.order_by("-pub_date")[:settings.NUM_OF_POSTS_ON_PAGE]
    posts = Post.objects.all()
    return render(request, template, {"posts": posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = "posts/group_list.html"
    # posts = group.posts.order_by("-pub_date")[:settings.NUM_OF_POSTS_ON_PAGE]
    posts = group.posts.all()[:settings.NUM_OF_POSTS_ON_PAGE]
    return render(request, template, {"group": group, "posts": posts})
