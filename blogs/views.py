from django.shortcuts import get_object_or_404, render

from models import Blog


def index(request):
    posts = Blog.objects.filter(visible=True).order_by("-created_on")[:5]
    return render(request, "blogs/index.html", {"posts_list": posts})


def detail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id, visible=True)
    return render(request, "blogs/detail.html", {"post": post})
