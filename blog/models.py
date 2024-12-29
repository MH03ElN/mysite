from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", default="/blog/defualt.jpg")
    category = models.ManyToManyField(Category)
    status = models.IntegerField(default=False)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
