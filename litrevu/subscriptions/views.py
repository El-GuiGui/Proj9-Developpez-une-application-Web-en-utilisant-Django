from django.shortcuts import render


def subscribe(request):
    return render(request, "subscriptions/subscribe.html")
