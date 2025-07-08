from django.urls import path
from website.views import *

urlpatterns = [
    path("website/", index_veiw),
    path("about/", about_veiw),
    path("contact/", contact_veiw),
]
