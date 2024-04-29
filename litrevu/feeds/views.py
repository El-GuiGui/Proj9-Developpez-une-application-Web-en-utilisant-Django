from django.shortcuts import render


def flux(request):
    return render(request, "feeds/flux.html")


def posts(request):
    return render(request, "feeds/posts.html")
