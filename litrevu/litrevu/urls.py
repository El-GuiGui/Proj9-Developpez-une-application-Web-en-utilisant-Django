from django.contrib import admin
from django.urls import path
from authentification.views import authentification, inscription
from tickets.views import create_ticket, edit_ticket
from reviews.views import create_review, modify_review, create_reponse_review
from subscriptions.views import subscribe

urlpatterns = [
    path("admin/", admin.site.urls),
    path("authentification/login.html", authentification),
    path("authentification/signup.html", inscription),
    path("tickets/create_ticket.html", create_ticket),
    path("tickets/edit_ticket.html", edit_ticket),
    path("reviews/create_review.html", create_review),
    path("reviews/modify_review.html", modify_review),
    path("reviews/create_reponse_review.html", create_reponse_review),
    path("subscriptions/subscribe.html", subscribe),
]
