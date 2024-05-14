from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    image = models.ImageField(upload_to="tickets/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    headline = models.CharField(max_length=255)
    rating = models.IntegerField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
