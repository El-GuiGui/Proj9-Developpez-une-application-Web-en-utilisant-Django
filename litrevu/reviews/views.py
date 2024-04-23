from django.shortcuts import render


def create_review(request):
    return render(request, "reviews/create_review.html")


def create_reponse_review(request):
    return render(request, "reviews/create_reponse_review.html")


def modify_review(request):
    return render(request, "reviews/modify_review.html")
