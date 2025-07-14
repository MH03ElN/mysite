from django.shortcuts import render
from blog.models import Post


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    post = Post.objects.get(id=pid)
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)
