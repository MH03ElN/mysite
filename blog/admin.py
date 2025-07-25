from django.contrib import admin
from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ("title", "status", "published_date", "created_date")
    list_filter = ("status",)
    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)
