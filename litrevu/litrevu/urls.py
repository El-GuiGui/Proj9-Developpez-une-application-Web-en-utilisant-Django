from django.contrib import admin
from django.urls import path
from authentification.views import authentification, inscription
from tickets.views import create_ticket, edit_ticket
from reviews.views import create_review, modify_review, create_reponse_review
from subscriptions.views import subscribe
from feeds.views import flux, posts, delete_review
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("authentification/login.html", authentification, name="login"),
    path("authentification/signup.html", inscription, name="signup"),
    path("tickets/create_ticket.html", create_ticket, name="create_ticket"),
    path("tickets/edit_ticket.html", edit_ticket, name="edit_ticket"),
    path("reviews/create_review.html", create_review, name="create_review"),
    path("modify_review/<int:review_id>/", modify_review, name="modify_review"),
    path("reviews/create_reponse_review.html", create_reponse_review, name="create_reponse_review"),
    path("subscriptions/subscribe.html", subscribe, name="subscribe"),
    path("feeds/posts.html", posts, name="posts"),
    path("delete_review/<int:review_id>/", delete_review, name="delete_review"),
    path("feeds/flux.html", flux, name="flux"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
