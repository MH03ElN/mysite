from django.shortcuts import render


def index_view(requests):
    return render(requests, "website/index.html")


def about_view(requests):
    context = {"name": "hosein", "last_name": "karbasi"}
    return render(requests, "website/about.html", context)


def contact_view(requests):
    return render(requests, "website/contact.html")
