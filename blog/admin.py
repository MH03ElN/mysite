from django.contrib import admin
from blog.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("status",)
    list_display = ("id", "title", "status", "created_date")
    search_fields = ["title", "content"]
    date_hierarchy = "created_date"


admin.site.register(Post, PostAdmin)
