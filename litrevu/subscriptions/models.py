from django.conf import settings
from django.db import models


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ("user", "followed_user")

    def __str__(self):
        return f"{self.user.username} follows {self.followed_user.username}"
