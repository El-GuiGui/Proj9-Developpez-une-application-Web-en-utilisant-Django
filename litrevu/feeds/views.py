from django.shortcuts import render
from reviews.models import Review, Ticket
from itertools import chain
from subscriptions.models import UserFollows
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from reviews.models import Review
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404


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

    return render(request, "feeds/posts.html", {"my_reviews": reviews, "my_tickets": tickets})


@csrf_exempt
def delete_ticket(request, ticket_id):
    if request.method == "POST":
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if ticket.user == request.user:
            ticket.delete()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Unauthorized"}, status=403)
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def delete_review(request, review_id):
    if request.method == "POST":
        review = get_object_or_404(Review, id=review_id)
        if review.user == request.user:
            review.delete()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Unauthorized"}, status=403)
    return JsonResponse({"error": "Invalid request method"}, status=400)
