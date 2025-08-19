from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1)[:3]
    return {'posts':posts}