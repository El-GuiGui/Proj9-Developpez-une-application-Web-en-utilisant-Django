from django.shortcuts import render
from reviews.models import Review, Ticket
from itertools import chain
from subscriptions.models import UserFollows
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from reviews.models import Review
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def flux(request):
    followed_ids = UserFollows.objects.filter(user=request.user).values_list("followed_user_id", flat=True)
    print("Followed IDs:", followed_ids)

    tickets = Ticket.objects.filter(user_id__in=followed_ids)
    print("Tickets:", tickets)

    reviews = Review.objects.filter(user_id__in=followed_ids)
    print("Reviews:", reviews)

    posts = sorted(chain(tickets, reviews), key=lambda post: post.created_at, reverse=True)
    print("Posts:", posts)

    return render(request, "feeds/flux.html", {"posts": posts})


@login_required
def posts(request):
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)

    posts = sorted(list(reviews) + list(tickets), key=lambda x: x.created_at, reverse=True)
    return render(request, "feeds/posts.html", {"my_posts": posts})


@csrf_exempt
def delete_review(request, review_id):
    if request.method == "DELETE":
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return HttpResponse("Supprimé", status=204)
    return HttpResponse("Méthode non autorisée", status=405)


def modify_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        return redirect("flux")
    return render(request, "reviews/modify_review.html", {"review": review})
