from django.shortcuts import render


# Create your views here.
def index_view(requests):
    return render(requests, "website/index.html")


def about_view(requests):
    return render(requests, "website/about.html")


def contact_view(requests):
    return render(requests, "website/contact.html")
