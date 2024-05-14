from django.shortcuts import render
from .models import Ticket, Review
from django.contrib.auth.models import User


def flux(request):
    followed_users = User.objects.filter(followers__follower=request.user)

    tickets = Ticket.objects.filter(user__in=followed_users | User.objects.filter(id=request.user.id))
    reviews = Review.objects.filter(user__in=followed_users | User.objects.filter(id=request.user.id))

    posts = sorted(list(tickets) + list(reviews), key=lambda post: post.created_at, reverse=True)

    return render(request, "reviews/flux.html", {"posts": posts})
