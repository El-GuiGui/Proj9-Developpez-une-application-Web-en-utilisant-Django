from django.shortcuts import render
from reviews.models import Review, Ticket
from itertools import chain
from subscriptions.models import UserFollows
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from reviews.models import Review
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User


@login_required
def flux(request):
    followed_users = UserFollows.objects.filter(user=request.user).values_list("followed_user_id", flat=True)

    # Tickets des utilisateurs suivis
    followed_tickets = Ticket.objects.filter(user_id__in=followed_users)

    # Critiques des utilisateurs suivis
    followed_reviews = Review.objects.filter(user_id__in=followed_users)

    # Critiques en réponse aux tickets des utilisateurs suivis
    reviews_of_followed_tickets = Review.objects.filter(ticket__user_id__in=followed_users)

    # Critiques en réponse aux tickets de l'utilisateur connecté
    my_ticket_reviews = Review.objects.filter(ticket__user=request.user)

    # Posts de l'utilisateur connecté
    my_tickets = Ticket.objects.filter(user=request.user)
    my_reviews = Review.objects.filter(user=request.user)

    # Ajouter une liste des tickets qui ont déjà une critique
    tickets_with_reviews = [review.ticket.id for review in Review.objects.all()]
    followed_tickets = followed_tickets.exclude(id__in=reviews_of_followed_tickets.values_list("ticket_id", flat=True))
    # Combiner et trier les posts
    posts = sorted(
        chain(followed_tickets, followed_reviews, reviews_of_followed_tickets),
        key=lambda post: post.created_at,
        reverse=True,
    )

    return render(request, "feeds/flux.html", {"posts": posts, "tickets_with_reviews": tickets_with_reviews})


@login_required
def posts(request):
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user).exclude(id__in=reviews.values_list("ticket_id", flat=True))

    posts = sorted(list(reviews) + list(tickets), key=lambda x: x.created_at, reverse=True)
    return render(request, "feeds/posts.html", {"my_posts": posts})


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
