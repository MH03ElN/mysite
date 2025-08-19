from django.shortcuts import render
from blog.models import Post


# Create your views here.
def blog_view(request, cat_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    post = Post.objects.get(id=pid)
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)


# def blog_category(request, cat_name):
#     posts = Post.objects.filter(category__name=cat_name)
#     context = {"posts":posts}
#     return render(request, "blog/blog-home.html", context)
