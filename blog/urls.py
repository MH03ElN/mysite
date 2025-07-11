from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("", blog_view),
    path("single/", blog_single),
]
