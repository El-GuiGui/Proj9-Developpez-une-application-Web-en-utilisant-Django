from django.http import HttpResponse
from django.shortcuts import render


def authentification(request):
    return render(request, "authentification/authentification.html")


def inscription(request):
    return render(request, "authentification/inscription.html")


def connexion(request):
    return render(request, "authentification/connexion.html")
