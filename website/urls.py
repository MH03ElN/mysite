from django.urls import path ,include
from website.views import *

urlpatterns = [
    path('' , index_view),
    path('about/' , about_view),
    path('contact/' , contact_view),
]
