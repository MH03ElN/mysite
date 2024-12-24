from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.IntegerField(default=False)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

        def __str__(self):
            return self.title
