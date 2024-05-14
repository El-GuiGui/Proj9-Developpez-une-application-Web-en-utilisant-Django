from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def create_review(request):
    if request.method == "POST":
        ticket_id = request.POST.get("ticket_id")
        ticket = Ticket.objects.get(id=ticket_id)
        Review.objects.create(
            ticket=ticket,
            user=request.user,
            headline=request.POST.get("review_headline"),
            rating=request.POST.get("rating"),
            body=request.POST.get("review_body"),
        )
        return redirect("flux")
    return render(request, "reviews/create_review.html")


@login_required
def create_reponse_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        Review.objects.create(
            ticket=ticket,
            user=request.user,
            headline=request.POST.get("review_headline"),
            rating=request.POST.get("rating"),
            body=request.POST.get("review_body"),
        )
        return redirect("flux")
    return render(request, "reviews/create_response_review.html", {"ticket": ticket})


def modify_review(request):
    return render(request, "reviews/modify_review.html")


def flux(request):
    followed_users = User.objects.filter(followers__follower=request.user).values_list("id", flat=True)

    reviews = Review.objects.filter(user_id__in=list(followed_users) + [request.user.id])
    tickets = Ticket.objects.filter(user_id__in=list(followed_users) + [request.user.id])

    posts = sorted(chain(reviews, tickets), key=lambda post: post.created_at, reverse=True)

    return render(request, "feeds/flux.html", {"posts": posts})
