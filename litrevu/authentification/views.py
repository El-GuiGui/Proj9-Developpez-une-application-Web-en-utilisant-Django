from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse


def authentification(request):
    return render(request, "authentification/authentification.html")


def inscription(request):
    return render(request, "authentification/inscription.html")


def connexion(request):
    return render(request, "authentification/connexion.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Cet utilisateur existe déjà")
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect("flux")
        else:
            return HttpResponse("Les mots de passe ne correspondent pas")
    else:
        return render(request, "authentification/inscription.html")
