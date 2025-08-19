from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag("blog/blog-latest-posts.html")
def latestposts():
    posts = Post.objects.filter(status=1)[:3]
    return {"posts": posts}


@register.inclusion_tag("blog/blog-post-categories.html")
def categories():
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = Post.objects.filter(status=1, category=name).count()
    return {"categories": cat_dict}
