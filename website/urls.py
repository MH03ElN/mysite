from django.urls import path
from website.views import *

name = "website"

urlpatterns = [
    path("", index_view, name="index"),
    path("about/", index_view, name="index"),
    path("contact/", index_view, name="index"),
]
