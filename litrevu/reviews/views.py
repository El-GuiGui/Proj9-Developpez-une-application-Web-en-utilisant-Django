from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReviewForm, TicketForm


@login_required
def create_review(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("flux")
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
    return render(request, "reviews/create_review.html", {"ticket_form": ticket_form, "review_form": review_form})


@login_required
def create_reponse_review(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("flux")
    else:
        review_form = ReviewForm()
    return render(request, "reviews/create_reponse_review.html", {"review_form": review_form, "ticket": ticket})


@login_required
def modify_review(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = ReviewForm(instance=review)
    return render(request, "reviews/modify_review.html", {"form": form, "review": review})


def flux(request):
    followed_users = User.objects.filter(followers__follower=request.user).values_list("id", flat=True)

    reviews = Review.objects.filter(user_id__in=list(followed_users) + [request.user.id])
    tickets = Ticket.objects.filter(user_id__in=list(followed_users) + [request.user.id])

    posts = sorted(chain(reviews, tickets), key=lambda post: post.created_at, reverse=True)

    return render(request, "feeds/flux.html", {"posts": posts})
