from django.urls import path
from website.views import *

app_name = "website"

urlpatterns = [
    path("", index_view),
    path("about/", about_view),
    path("contact/", contact_view),
]
