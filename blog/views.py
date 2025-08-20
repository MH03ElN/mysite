from django.shortcuts import render
from blog.models import Post


# Create your views here.
def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    post = Post.objects.get(id=pid)
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)



