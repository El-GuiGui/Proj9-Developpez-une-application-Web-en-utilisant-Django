from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse


def authentification(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("flux")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, "authentification/authentification.html")


def inscription(request):
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
